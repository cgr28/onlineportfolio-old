from django.shortcuts import render
from experience.models import Experience
# Create your views here.
def index(request):
    experiences = Experience.objects.all()
    pro_exps = []
    club_exps = []
    ed_exps = []

    for experience in experiences:
        if experience.type == "proffesional":
            pro_exps.append(experience)
        elif experience.type == "club":
            club_exps.append(experience)
        else:
            ed_exps.append(experience)

    context = {
        "jobs": pro_exps,
        "clubs": club_exps,
        "schools": ed_exps, 
    }
    return render(request, "experience/experience.html", context)