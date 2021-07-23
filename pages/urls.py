from django.urls import path
from . import views


urlpatterns = [
    # app pages
    path('<int:page_id>/', views.page, name="page"),
]
