from django.urls import path
from . import views

app_name = 'resume' 
urlpatterns = [
    path('generate/', views.generate_resume),
]

