from django.db import models

class Folder(models.Model):
    folder_name = models.CharField(max_length=50)
    creator = models.ForeignKey("Muser", on_delete=models.CASCADE, related_name="folders")
    