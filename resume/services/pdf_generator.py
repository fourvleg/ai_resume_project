from django.template.loader import render_to_string
from weasyprint import HTML
import os
from django.conf import settings

def render_resume_to_pdf(resume):
    html_string = render_to_string("resume/pdf_template.html", {"resume": resume})

    pdf_file_name = f"{resume.full_name.replace(' ', '_')}_resume.pdf"
    pdf_path = os.path.join(settings.MEDIA_ROOT, "resumes", pdf_file_name)

    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

    HTML(string=html_string).write_pdf(pdf_path)

    return f"{settings.MEDIA_URL}resumes/{pdf_file_name}"
