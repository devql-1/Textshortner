
from django.urls import path

from . import views
from .views import model

urlpatterns = [
    path('',views.model),
]