from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    tag_name = models.CharField(max_length=50)

class Muser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100)

    @property
    def username(self):
        return f"{self.user.username}"

    
class Folder(models.Model):
    folder_name = models.CharField(max_length=50)
    creator = models.ForeignKey(Muser, on_delete=models.CASCADE, null=True)

class Image(models.Model):
    description = models.CharField(max_length=100)
    img_url = models.URLField()
    muser = models.ForeignKey(Muser, on_delete=models.CASCADE)

class ImageFolder(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='image_folder')

class ImageTag(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='image_tag')

