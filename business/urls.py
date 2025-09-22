from django.urls import path
from . import views

app_name = "business"

urlpatterns = [
    path("", views.business, name="business"),
    path("honda/", views.honda, name="honda"),
    path("toyota/", views.toyota, name="toyota"),
    path("lexus/", views.lexus, name="lexus"),
    path("index/",views.index, name="index"),
    path("post/",views.post, name="post"),
]
