from django.contrib.auth.models import User
from django.db import models

class MLModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ml_models")
    name = models.CharField(max_length=50, unique=True)
    model_file = models.FileField(upload_to='ml_models/')
    created_at = models.DateTimeField(auto_now_add=True)


class TrainingImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="training_images")
    image_file = models.ImageField(upload_to='training_images/')


class GeneratedImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="generated_images")
    model = models.ForeignKey(MLModel, on_delete=models.CASCADE, related_name="generated_images")
    image_file = models.ImageField(upload_to='generated_images/')
    created_at = models.DateTimeField(auto_now_add=True)
