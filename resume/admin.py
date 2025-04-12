from django.contrib import admin
from .models import Resume, Experience, Skill, Education

registered_models = [Resume, Experience, Skill, Education]

admin.site.register(registered_models)