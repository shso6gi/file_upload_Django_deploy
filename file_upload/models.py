from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    file_name = models.TextField()
    file_hash = models.CharField(max_length=50)
    file_size = models.IntegerField()
    file_upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name
