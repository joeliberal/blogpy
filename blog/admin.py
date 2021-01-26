from django.contrib import admin

# Register your models here.
from .models import Category,UserProfile,Article


admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(Article)

