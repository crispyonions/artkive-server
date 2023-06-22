from django.db import models

class ImageTag(models.Model):
    image = models.ForeignKey("Image", on_delete=models.CASCADE)
    tag = models.ForeignKey("Tag", on_delete=models.CASCADE)

