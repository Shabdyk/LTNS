from django.db import models

# Create your models here.

class UserID(models.Model):
    user_id = models.CharField(max_length=10)
    imported = models.ForeignKey("ImportFile", on_delete=models.CASCADE, default=None)
    exported = models.ForeignKey("ExportFile", on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.user_id

class ImportFile(models.Model):
    
    file = models.FileField(upload_to='imports/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

class ExportFile(models.Model):
    source = models.ForeignKey("ImportFile", on_delete=models.CASCADE, default=None)
    file = models.FileField(upload_to='exports/', default=None)

    def __str__(self):
        return self.file.name
