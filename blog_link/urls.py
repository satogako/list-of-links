from . import views
from django.urls import path


urlpatterns = [
    path('', views.ResourceList.as_view(), name='all_resources'),
    path('modal1/', views.modal_view, name='modal1')
]
