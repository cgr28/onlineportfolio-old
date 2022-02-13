from django.shortcuts import get_object_or_404, render
from projects.models import Project

# Create your views here.
def projects(request):
    projects = Project.objects.all()
    context = {
        "project": projects
    }
    return render(request, "projects/projects.html", context)

def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    context = {
        "project": project
    }
    return render(request, "projects/project.html", context)