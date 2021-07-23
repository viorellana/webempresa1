from django.urls import path
from . import views


urlpatterns = [
    # app services
    path('', views.services, name='services'),
]