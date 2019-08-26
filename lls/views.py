from django.shortcuts import render
from django.http import HttpResponse
from . forms import UserForm
from . models import Topic

def index(request):
    if request.method == "POST":
        topic = request.POST.get("topic")
        tpc=Topic()
        tpc.text=topic
        #tpc.owner='misha'
        tpc.owner = request.user   # скатано у эрика
        tpc.save()
        return HttpResponse("Сохранена тема :  <h2>{0}</h2>".format(topic))
    else:
        userform = UserForm()
        return render(request, "lls/index.html", {"form": userform})

