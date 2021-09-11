from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.request_login, name="request_login"),
    path("logout", views.request_logout, name="request_logout"),
]