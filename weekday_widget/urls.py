from django.urls import path
from .views import today_view

app_name = "weekday_widget"

urlpatterns = [
    path("", today_view, name="today"),   # /weekday/
]
