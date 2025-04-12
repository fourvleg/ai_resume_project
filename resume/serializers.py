from rest_framework import serializers
from .models import Resume, Education, Experience, Skill

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['company_name', 'position', 'start_date', 'end_date', 'description']

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['skill_name']

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['institution_name', 'degree', 'start_date', 'end_date']

class ResumeSerializer(serializers.ModelSerializer):
    experiences = ExperienceSerializer(many=True, read_only=False)
    skills = SkillSerializer(many=True, read_only=False)
    educations = EducationSerializer(many=True, read_only=True)
    
    class Meta:
        model = Resume
        fields = ['full_name', 'desired_position', 'summary', 'education', 'experiences', 'skills', 'educations']