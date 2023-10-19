from django.db import models
from users.models import CustomUser


class PostTopic(models.Model):
    name = models.CharField('Название', max_length=160)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=160)
    text = models.TextField('Текст')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post_topic = models.ForeignKey(PostTopic, on_delete=models.CASCADE, null=True)
    cover_img = models.ImageField(blank=False, upload_to='post_covers/')


