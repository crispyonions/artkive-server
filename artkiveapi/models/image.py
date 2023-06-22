from django.db import models

class Image(models.Model):
    description = models.CharField(max_length=100)
    img_url = models.URLField()
    muser = models.ForeignKey("Muser", on_delete=models.CASCADE, related_name="muser")
    tags = models.ManyToManyField("Tag", through = "ImageTag", related_name= "tags")
    folder = models.ForeignKey("Folder", on_delete=models.CASCADE, related_name="image_folder", null=True)
    