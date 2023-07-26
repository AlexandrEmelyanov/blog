from django.db import models
from users.models import User


class Posts(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return {self.title}
