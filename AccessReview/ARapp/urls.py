from django.urls import path, include
from django.contrib import admin

from . import views

app_name = "ARapp"
urlpatterns = [
    # ex: /ARapp/
    #path("", views.home, name="index")
    path("index/", views.index, name="index"),
    path("users/", views.UsersListView.as_view(), name="all_users"),
    path("about/", views.about, name="about"),
    path("reviewList/", views.ReviewListListView.as_view(), name="reviewList"),
    path("systemAdmin/reviewListAdd/", views.ReviewListAdd, name="reviewListAdd"),
    path("systemAdmin/countries/", views.CountriesListView.as_view(), name="countries"),
    path("countryAdd/", views.CountryAddForm, name="countryAdd"),
    path("submit/reviewListAdd/", views.ReviewListSubmit, name="submit_reviewListAdd"),
    path("systems/", views.SystemsListView.as_view(), name="systems"),
    path("systems/<int:pk>", views.SystemDetailView.as_view(), name="system_detail"),
    path("systems/<int:pk>/countries/", views.CountryListView.as_view(), name="system_country_view"),
    path("temp_review/", views.temp_review, name="temp_rev")

    # path("systems/", views.systems, name="systems"),
    #path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    #path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    #path("<int:question_id>/vote/", views.vote, name="vote"),
]