from django.urls import path, include
from . import views

app_name = 'resume' 
urlpatterns = [
    path('generate/', views.generate_resume),
]

