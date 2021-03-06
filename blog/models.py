from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='опубликовано')


class Post(models.Model):
    STATUS_CHOICES = (
        ("черновик", "Черновик"),
        ("опубликовано", "опубликовано"),
    )
    title = models.CharField(max_length=250, verbose_name="Название ")
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField(verbose_name="Статья")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager()  # Менеджер по умолчанию.
    published = PublishedManager()  # Наш новый менеджер

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year,
                        self.publish.month, self.publish.day, self.slug])
