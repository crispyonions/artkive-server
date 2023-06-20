# Generated by Django 4.2.2 on 2023-06-20 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artkiveapi', '0005_alter_image_description_alter_image_folders_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='folders',
        ),
        migrations.RemoveField(
            model_name='image',
            name='tags',
        ),
        migrations.AlterField(
            model_name='folder',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
