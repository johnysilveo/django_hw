from django.urls import path
from . import views

app_name = 'sports'
urlpatterns = [
    path("",views.sports,name="sports"),
    path("basketball",views.basketball,name="basketball"),
    path("football",views.football,name="football"),
    path("hokey/",views.hokey,name="hokey"),
    path("tickets/buy/", views.buy_tickets, name="buy_tickets"),
    path("tickets/thanks/", views.ticket_thanks, name="ticket_thanks"),
]