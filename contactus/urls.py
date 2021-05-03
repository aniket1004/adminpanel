from django.urls import path
from . import views

urlpatterns = [
    path('',views.MessageAPI),
    path('<str:pk>/',views.MessageDelete)
]
