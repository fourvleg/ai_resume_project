from openai import OpenAI
import json

# Инициализация клиента с новым синтаксисом
client = OpenAI(api_key="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")

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)


def generate_resume_data(full_name, position, skills):
    prompt = f"""
Ты — профессиональный карьерный консультант. Сгенерируй краткое резюме, опыт работы (2-3 места), и образование для соискателя.
Дано:
- Имя: {full_name}
- Позиция: {position}
- Навыки: {', '.join(skills)}

Ответ верни строго в JSON формате:
{{
  "summary": "Краткое описание",
  "experience": [
    {{
      "company": "Название компании",
      "position": "Должность",
      "start_date": "ГГГГ-ММ-ДД",
      "end_date": "ГГГГ-ММ-ДД",
      "description": "Чем занимался"
    }},
    ...
  ],
  "education": "Описание образования (университет, факультет, годы)"
}}
"""

    response = client.chat.completions.create(
        model="deepseek/deepseek-chat:free",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        response_format={"type": "json_object"}  # Убедитесь, что ответ будет в JSON
    )

    # Извлекаем JSON из ответа (новый синтаксис)
    content = response.choices[0].message.content
    
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        # Если возникла ошибка парсинга, возвращаем структуру с ошибкой
        return {
            "error": "Не удалось распарсить ответ",
            "raw_response": content
        }
