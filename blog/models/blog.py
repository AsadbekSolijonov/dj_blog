from django.db import models

from config.settings import AUTH_USER_MODEL
from django_ckeditor_5.fields import CKEditor5Field


class Blog(models.Model):
    TYPE = {
        'Jounal': 'Journal',
        "Life updates": 'Life updates',
        'Travel stories': 'Travel stories',
        'Personal growth': 'Personal growth'
    }
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='Sarlavha')
    content = CKEditor5Field(verbose_name='Tavsif')
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    type = models.CharField(max_length=50, choices=TYPE, default='Jounal')
    created_at = models.DateTimeField(auto_now_add=True)  # 2025-06-19 16:28
    updated_at = models.DateTimeField(auto_now=True)  # 2025-06-22 15:28

    def __str__(self):
        return f"{self.id} {self.title}"

    class Meta:
        permissions = [
            ('can_all_manage', 'Can all changed models')
        ]


class Comment(models.Model):
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    message = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.author:
            return f"{self.author.username}: {self.message[:30]}"
        return f"{self.message[:30]}"

    class Meta:
        ordering = ['-created_at']
