from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from ckeditor.fields import RichTextField


def validate_file_extention(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]
    valid_extention = ['.jpg', '.png']
    if not ext.lower() in valid_extention:
        raise ValidationError('unsoported .....')


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='file/user_avatar/', validators=[validate_file_extention])
    description = models.CharField(max_length=300)


class Article(models.Model):
    title = models.CharField(max_length=120)
    cover = models.FileField(upload_to='file/article_cover/', validators=[validate_file_extention])
    content = RichTextField()
    creste_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    promote = models.BooleanField(default=False)
    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100)
    cover = models.FileField(upload_to='file/category_cover/', validators=[validate_file_extention])

    def __str__(self):
        return self.title