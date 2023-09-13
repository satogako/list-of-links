from . import views
from django.urls import path


urlpatterns = [
    path('', views.ResourceList.as_view(), name='all_resources'),
    path('categories/', views.TagsList.as_view(), name='categories'),
    path('resource-list/', views.ResourceListAPIView.as_view(), name='resource-list'),
    #path('categories/', views.categories, name='categories'),
    path('<slug:slug>/', views.ResourceDetails.as_view(), name='resource_comments'),
    path('like/<slug:slug>', views.ResourseAdmirers.as_view(), name='post_admirer'),
]
