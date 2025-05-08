from django.db import models
from django.contrib.auth.models import User


# 用户信息表模型
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return self.user.username


# 宠物信息表模型
class Pet(models.Model):
    STATUS_CHOICES = [
        ("available", "可领养"),
        ("adopted", "已领养"),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    species = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# 领养申请表模型
class AdoptionRequest(models.Model):
    STATUS_CHOICES = [
        ("pending", "待审核"),
        ("approved", "已批准"),
        ("cancelled", "已取消"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# 宠物图片表模型
class PetImage(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
