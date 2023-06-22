from django.db import models

class ImageFolder(models.Model):
    image = models.ForeignKey("Image", on_delete=models.CASCADE, related_name="image")
    folder = models.ForeignKey("Folder", on_delete=models.CASCADE, related_name="imagefolder")