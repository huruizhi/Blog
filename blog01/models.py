from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags
import markdown

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    excerpt = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField('Tag', blank=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "title:%s, user:%s, create_time:%s" % (self.title, self.author, self.created_time)

    def get_absolute_url(self):
        return reverse("detail",  kwargs={'pk': self.pk})

    def auto_add_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        # 如果没有填写摘要
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt = "%s%s" % (strip_tags(md.convert(self.body))[:140], "...")
        # 调用父类的 save 方法将数据保存到数据库中
        super(Post, self).save(*args, **kwargs)

