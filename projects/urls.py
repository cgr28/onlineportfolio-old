from django.urls import path

from . import views

app_name="projects"

urlpatterns = [
    path('', views.projects, name='projects'),
    path('project/<int:project_id>', views.project, name='project'),
]