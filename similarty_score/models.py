from django.db import models
import os
# Create your models here.

def resume_upload_path(instance, filename):
    """Generates a file path for uploaded resumes"""
    return os.path.join("resumes", filename)

class ResumeUpload(models.Model):
    file = models.FileField(upload_to=resume_upload_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Resume uploaded on {self.uploaded_at.strftime('%Y-%m-%d %H:%M:%S')}"
