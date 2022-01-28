from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(),
                               on_delete= models.CASCADE,
                               )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])

class Comment(models.Model):
    article = models.ForeignKey(Article,
                                on_delete= models.CASCADE,
                                related_name= 'comment',
                                )
    com = models.TextField()
    author = models.ForeignKey(get_user_model(),
                               on_delete= models.CASCADE,
                               )

    def __str__(self):
        return self.com

    def get_absolute_url(self):
        return reverse('article_list')