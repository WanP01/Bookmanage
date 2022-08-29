from django.urls import path
from books import views

urlpatterns = [
    path('index/',views.index),
]