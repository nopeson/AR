from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.urls import reverse
from django.views import generic

import django_tables2 as tables

from .models import Users, UsersTable
from .models import Systems, SystemsTable
from .models import Country, CountryTable, CountryAddForm
from .models import R_ReviewList, ReviewListTable, ReviewListForm
from .urls import *
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

def ReviewListAdd(request):
    context = {}
    context['add_new_review_form'] = ReviewListForm()
    return render(request, "ARapp/systemAdmin/reviewList_add.html", context)


def ReviewListSubmit(request):
    if request.method == 'POST':
        d = ReviewListForm(request.POST)
        d.save()
    return render(request, "ARapp/index.html")

def CountryAdd(request):
    context = {}
    context['add_new_coutry_form'] = CountryAddForm()
    return render(request, "ARapp/country_add.html", context)            

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

class CountriesListView(tables.SingleTableView):
    model = Country
    table_class = SystemsTable
    context_object_name = "all_countries"
    template_name = "ARapp/systemAdmin/countries.html"    
 

class ReviewListListView(tables.SingleTableView):
    model = R_ReviewList
    table_class = SystemsTable
    context_object_name = "reviewListList"
    template_name = "ARapp/reviewList.html"
    

class SystemDetailView(generic.DetailView):
    model = Systems
    context_object_name = "system"
    #by defualt uses template_name = "ARapp/Systems_detail.html"


class CountryListView(tables.SingleTableView):
    model = Country
    table_class = CountryTable
    context_object_name = "countries_for_system"
    template_name = "ARapp/systems_countries.html"