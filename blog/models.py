from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # 2025-06-19 16:28
    updated_at = models.DateTimeField(auto_now=True)  # 2025-06-22 15:28

    def __str__(self):
        return f"{self.id} {self.title}"
