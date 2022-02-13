from django.shortcuts import render
from home.models import Skills

# Create your views here.
def index(request):
    skills = Skills.objects.all()
    context = {
        "skills": skills,
    }
    return render(request, 'home/index.html', context)
