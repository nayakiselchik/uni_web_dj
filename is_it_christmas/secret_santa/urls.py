from django.urls import path
from . import views

urlpatterns = [
    path("", views.is_it_christmas_today, name="home"),
    path("secret-santa/", views.game, name="game"),
    path(
        "secret-santa/delete-all/",
        views.delete_all_participants,
        name="delete_all_participants",
    ),
]
