from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create_poll, name="create"),
    path("retrieve", views.retrieve_poll, name="retrieve"),
    path("update", views.update_poll, name="update"),
    path("delete", views.delete_poll, name="delete"),
]