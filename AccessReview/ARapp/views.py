from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.urls import reverse
from django.views import generic

import django_tables2 as tables

from .models import Users, UsersTable
from .models import Systems, SystemsTable
from .models import Country, CountryTable
# Create your views here.


def index(request):
    return render(request, "ARapp/index.html")

def about(request):
    return render(request, "ARapp/about.html")

def temp_review(request):
    if request.method == 'POST':
        post_coutryID= request.POST["countryID"]
        post_systemID = request.POST["systemID"]
        dict = {
            'country': request.POST["countryID"],
            'system': request.POST["systemID"]
        }
    return render(request, "ARapp/temp_review.html", dict)
# def systems(request):
#     all_systems = Systems.objects.all()
#     context = {"all_systems" : all_systems}
#     return render(request, "ARapp/systems.html", context)
            

class UsersListView(tables.SingleTableView):
    model = Users
    table_class = UsersTable
    # queryset = Users.objects.all()
    context_object_name = "user_list"
    template_name = "ARapp/users.html"

class SystemsListView(tables.SingleTableView):
    model = Systems
    table_class = SystemsTable
    context_object_name = "all_systems"
    template_name = "ARapp/systems.html"

    ##TODO throughput tabulka - systems_country - read from that (maybe)

    # print(model.country.countryName)
    # print("aaa")
    # def get_queryset(self):
    #     """Return distinct systems"""
    #     return Systems.objects.all().values('systemName').distinct()

class SystemDetailView(generic.DetailView):
    model = Systems
    context_object_name = "system"
    # system_countries = Systems.objects.filter(systemName__iexact="Ledger")
    # context = {
    #     "systems_country_list":system_countries,
    # }
    # print(system_countries)

    #by defualt uses template_name = "ARapp/Systems_detail.html"


class CountryListView(tables.SingleTableView):
    model = Country
    table_class = CountryTable
    context_object_name = "countries_for_system"
    template_name = "ARapp/systems_countries.html"


""" 
class ResultsView(generic.DetailView):
    model = Users
    template_name = "ARapp/results.html"
 """