from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.urls import reverse
from django.views import generic

from .models import Users
# Create your views here.


def index(request):
    return render(request, "ARapp/index.html")

def about(request):
    return render(request, "ARapp/about.html")



class IndexView(generic.ListView):
    template_name = "ARapp/users.html"
    context_object_name = "user_list"
    data = Users.objects.all()

    def get_queryset(self):
        
        data = Users.objects.all()
        return data




""" 
class ResultsView(generic.DetailView):
    model = Users
    template_name = "ARapp/results.html"
 """