from django.db import models


class Resume(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    desired_position = models.CharField(max_length=255, verbose_name="Желаемая должность")
    summary = models.TextField(null=True, blank=True, verbose_name="Резюме")  # Краткое резюме, которое генерируется AI
    education = models.TextField(blank=True, null=True)  # Образование (если будет сгенерировано)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Резюме для {self.full_name} на позицию {self.desired_position}"

class Experience(models.Model):
    resume = models.ForeignKey(Resume, related_name="experiences", on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255, verbose_name="Название компании")
    position = models.CharField(max_length=255, verbose_name="Должность")
    start_date = models.DateField(null=True, blank=True, verbose_name="Дата начала")
    end_date = models.DateField(null=True, blank=True, verbose_name="Дата окончания")
    description = models.TextField(null=True, blank=True, verbose_name="Описание обязанностей")

    def __str__(self):
        return f"{self.position} в {self.company_name}"

class Skill(models.Model):
    resume = models.ForeignKey(Resume, related_name="skills", on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=255, verbose_name="Навыки")

    def __str__(self):
        return self.skill_name

class Education(models.Model):
    resume = models.ForeignKey(Resume, related_name="educations", on_delete=models.CASCADE)
    institution_name = models.CharField(max_length=255, verbose_name="Название учебного заведения")
    degree = models.CharField(max_length=255, verbose_name="Степень")
    start_date = models.DateField(null=True, blank=True, verbose_name="Дата начала")
    end_date = models.DateField(null=True, blank=True, verbose_name="Дата окончания")

    def __str__(self):
        return f"{self.degree} от {self.institution_name}"
