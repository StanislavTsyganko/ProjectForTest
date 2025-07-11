from django.urls import path
from . import views

app_name = 'citate'

urlpatterns = [
    path('', views.work_with_citates, name="citates"),
    path('add/', views.add_citate, name="add"),
    path('top', views.top_citate, name="top"),
]