from django.urls import path

from . import views

app_name = "ARapp"
urlpatterns = [
    # ex: /ARapp/
    #path("", views.home, name="index")
    path("", views.index, name="index"),
    path("users/", views.IndexView.as_view(), name="all_users"),
    #path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    #path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    #path("<int:question_id>/vote/", views.vote, name="vote"),
]