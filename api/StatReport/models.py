from django.db import models

class StatReport(models.Model):
    report_name = models.CharField(max_length=255)
    description = models.TextField()
    generated_at = models.DateTimeField(auto_now_add=True)
    file_path = models.CharField(max_length=255)

    def __str__(self):
        return self.report_name
