from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('visualization/<str:chart>/', views.visualization, name='visualization'),
]
