from django.urls import path
from App1.views import HomeView #Se importa la vista

urlpatterns = [
    path("", HomeView)
]