from django.shortcuts import render
from resume.models import Resume
# Create your views here.

def index(request):
    resume = Resume.objects.all()
    context = {
        "resumes": resume,
    }
    return render(request, "resume/resume.html", context)