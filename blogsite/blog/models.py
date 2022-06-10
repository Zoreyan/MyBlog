from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    show = models.BooleanField(default=0)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-added_at']

    def __str__(self):
        return self.title

    