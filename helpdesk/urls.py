from django.urls import path
from . import views

app_name = 'helpdesk'

urlpatterns = [
    path('', views.home, name='home'),
    path('app/<str:app_name>/', views.app_detail, name='app_detail'),
    path('yourguide/', views.yourguide, name='yourguide'),
]
