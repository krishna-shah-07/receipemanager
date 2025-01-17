from django.urls import path
from home.views import *

urlpatterns = [
    path("receipes/", ReceipeAPI.as_view(), name="receipes"),
]