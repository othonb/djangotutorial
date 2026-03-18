from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create_poll, name="create"),
    path("retrieve", views.retrieve_poll, name="retrieve"),
    path("update", views.update_poll, name="update"),
    path("delete", views.delete_poll, name="delete"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]