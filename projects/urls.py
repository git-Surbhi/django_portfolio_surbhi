from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.project_index, name='project_index'),
    path('pro/<int:id>', views.single_proj, name='project'),
] 