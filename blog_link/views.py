from django.shortcuts import render
from django.views import generic
from .models import Resource

# Create your views here.
class ResourceList(generic.ListView):
    """
    Displays only those resources that have published. The results are 
    sorted in reverse. The resource list is split into 8 items per page.
    """
    model = Resource
    queryset = Resource.objects.filter(condition=1).order_by('-created_on')
    paginate_by = 8
    template_name = 'base.html'
    