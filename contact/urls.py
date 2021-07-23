from django.urls import path
from . import views


urlpatterns = [
    # app contact
    path('', views.contact, name='contact'),
]
