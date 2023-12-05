from django.db import models
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.shortcuts import reverse

from users.models import User


class PostCategory(models.Model):
    name = models.CharField(max_length=127, unique=True)
    post_counter = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()
        self.post_counter += 1

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Posts(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('index:post-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        # Если пост новый (еще не сохранен в базе)
        if self.pk is None:
            is_new = True
        else:
            is_new = False

        old_category = None

        # Если пост уже существует (обновляется), сохраняем старую категорию
        if not is_new:
            old_category = Posts.objects.get(pk=self.pk).category

        super().save(*args, **kwargs)

        # Если пост новый или категория изменена, увеличиваем счетчик
        if is_new or (old_category and old_category != self.category):
            self.category.post_counter += 1
            self.category.save()

        # Если категория изменена, уменьшаем счетчик старой категории
        if old_category and old_category != self.category:
            old_category.post_counter -= 1
            old_category.save()


# Обработчик сигнала post_delete, чтобы уменьшать счетчик при удалении поста
@receiver(post_delete, sender=Posts)
def update_post_counter(sender, instance, **kwargs):
    if instance.category:
        category = instance.category
        category.post_counter -= 1
        category.save()


# def save_post_counter(sender, instance, created, **kwargs):
#     if created:
#         instance.category.post_counter += 1
#         instance.category.save()
#
#
# post_save.connect(update_post_counter, sender=Posts)


class Comment(models.Model):
    author_com = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments')
    create_com = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author_com.username}: {self.content[:40]}'
