from django.db import models
from django.contrib.auth.models import User

class Muser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=50)

class Image(models.Model):
    description = models.TextField()
    img_url = models.URLField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Tag(models.Model):
    tag_name = models.CharField(max_length=50)

class ImageTag(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

class Folder(models.Model):
    folder_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ImageFolder(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
