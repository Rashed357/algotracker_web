from django.urls import path
from . import views

urlpatterns = [
    # The empty string '' means the root URL (the homepage)
    path('', views.solution_list, name='solution_list'),
]