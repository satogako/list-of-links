from . import views
from django.urls import path


urlpatterns = [
    path('', views.ResourceList.as_view(), name='all_resources'),
    path('categories/', views.modal_view, name='categories'),
    path('<slug:slug>/', views.ResourceDetails.as_view(), name='resourсe_details'),
]
