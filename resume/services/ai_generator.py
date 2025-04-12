import json
import re

from openai import OpenAI



# ai form https://openrouter
client = OpenAI(
  base_url="chat.openrouter.ai", 
  api_key="your_api_key_here",  #API
)


#промт для генерации(для ваших шаловливых ручек)
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
    )
    
    content = re.sub(r"```(?:json)?\n(.+?)```", r"\1", response.choices[0].message.content, flags=re.DOTALL)

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return {
            "error": "Не удалось распарсить ответ",
            "raw_response": content
        }
