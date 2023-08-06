from django.db import models
from django.shortcuts import reverse

from users.models import User


class Posts(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('index:post-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
