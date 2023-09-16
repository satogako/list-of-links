from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Resource, CommentResourse
from .forms import ResourseFormComment
from taggit.models import Tag
from rest_framework.generics import ListAPIView
from .serializers import ResourceSerializer


# Create your views here.
class ResourceList(generic.ListView):
    """
    Displays only those resources that have published. The results are 
    sorted in reverse. The resource list is split into 9 items per page.
    """
    model = Resource
    queryset = Resource.objects.filter(condition=1).order_by('-created_on')
    paginate_by = 9
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        resources = self.get_queryset()
        comments = []
        for resource in resources:
            comments.append(resource.comments.filter(approved=True).order_by('created_on'))
        context['comments'] = comments  
        return context


class TagsList(generic.ListView):
    model = Resource
    queryset = Resource.objects.filter(condition=1).order_by('-created_on')
    #paginate_by = 9
    template_name = 'categories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class ResourceListAPIView(ListAPIView):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class ResourceDetails(View):  
    
    def get(self, request, slug, *args, **kwargs):
        queryset = Resource.objects.filter(condition=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        admired = False
        if post.admirers.filter(id=self.request.user.id).exists():
            admired = True

        return render(
            request,
            "resource_details.htm",
            {
                "post": post,
                "comments": comments,
                "already_commented": False,
                "admired": admired,
                "form_comment": ResourseFormComment()     
            },
        )
    
    def post(self, request, slug, *args, **kwargs):
        queryset = Resource.objects.filter(condition=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        admired = False
        if post.admirers.filter(id=self.request.user.id).exists():
            admired = True

        form_comment = ResourseFormComment(data=request.POST)
        if form_comment.is_valid():
            form_comment.instance.email = request.user.email
            form_comment.instance.name = request.user.username
            comment = form_comment.save(commit=False)
            comment.post = post
            comment.save()
        else:
            form_comment = ResourseFormComment()

        return render(
            request,
            "resource_details.htm",
            {
                "post": post,
                "comments": comments,
                "already_commented": True,
                "admired": admired,
                "form_comment": ResourseFormComment()     
            },
        )


class ResourseAdmirers(View):
    def post(self, request, slug):
        resource = get_object_or_404(Resource, slug=slug)

        if resource.admirers.filter(id=request.user.id).exists():
            resource.admirers.remove(request.user)
        else:
            resource.admirers.add(request.user)

        return HttpResponseRedirect(reverse('resource_comments', args=[slug]))


class ApprovalCommentsView(UserPassesTestMixin, generic.ListView):
    """
    Displays comments that require approval. 
    """
    model = CommentResourse
    queryset = CommentResourse.objects.filter(approved=False)
    template_name = 'approval_comments.html'

    def test_func(self):
       return self.request.user.username == 'admin'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = CommentResourse.objects.filter(approved=True).order_by('-created_on')
        context['approved_comments'] = comments
        return context
    
    def post(self, request, *args, **kwargs):
        comments_to_approve = CommentResourse.objects.filter(id__in=request.POST.getlist('approve[]'))
        comments_to_approve.update(approved=True)
        comments_to_delete = CommentResourse.objects.filter(id__in=request.POST.getlist('delete[]'))
        comments_to_delete.delete()
        return super().get(request, *args, **kwargs)