from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Resource
from taggit.models import Tag

# Create your views here.
class ResourceList(generic.ListView):
    """
    Displays only those resources that have published. The results are 
    sorted in reverse. The resource list is split into 8 items per page.
    """
    model = Resource
    queryset = Resource.objects.filter(condition=1).order_by('-created_on')
    paginate_by = 9
    template_name = 'index.html'
    

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
                "admired": admired

            },
        )

