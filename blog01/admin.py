from django.contrib import admin
from blog01 import models

# Register your models here.

admin.site.register(models.Category)
admin.site.register(models.Post)
admin.site.register(models.Tag)
admin.site.register(models.UserInfo)
