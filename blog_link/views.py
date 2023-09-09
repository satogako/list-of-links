from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Resource
from .forms import ResourseFormComment
from taggit.models import Tag

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


def modal_view(request):
    return render(request, 'categories.html')



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
                "admired": admired,
                "form_comment": ResourseFormComment()     
            },
        )

