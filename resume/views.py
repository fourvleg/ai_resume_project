from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Resume, Experience, Skill
from .serializers import ResumeSerializer
from .services.ai_generator import generate_resume_data

@api_view(["POST"])
def generate_resume(request):
    data = request.data
    full_name = data.get("full_name")
    position = data.get("desired_position")
    skills = data.get("skills", [])

    if not full_name or not position:
        return Response({"error": "full_name and desired_position are required"}, status=400)

    # 🔸 Генерируем данные с помощью OpenAI
    try:
        ai_result = generate_resume_data(full_name, position, skills)
        print("AI Result:", ai_result)
    except Exception as e:
        return Response({"error": str(e)}, status=500)
    
    if "summary" not in ai_result:
        return Response({"error": "AI response missing 'summary' key", "ai_result": ai_result}, status=500)
    
    # 🔹 Создаём резюме
    resume = Resume.objects.create(
        full_name=full_name,
        desired_position=position,
        summary=ai_result["summary"],
        education=ai_result["education"]
    )

    # 🔹 Сохраняем опыт работы
    for exp in ai_result.get("experience", []):
        Experience.objects.create(
            resume=resume,
            company_name=exp["company"],
            position=exp["position"],
            start_date=exp["start_date"],
            end_date=exp.get("end_date"),
            description=exp["description"]
        )

    # 🔹 Сохраняем навыки
    for skill in skills:
        Skill.objects.create(resume=resume, skill_name=skill)

    # 🔸 Возвращаем сериализованные данные
    serializer = ResumeSerializer(resume)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

