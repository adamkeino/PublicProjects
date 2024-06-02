from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("fleet/detail", views.detail, name="detail")
]
