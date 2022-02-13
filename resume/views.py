from django.shortcuts import render
from resume.models import Resume
# Create your views here.

def index(request):
    resume = Resume.objects.all()
    context = {
        "resumes": resume,
    }
    print(resume[0].link)
    return render(request, "resume/resume.html", context)