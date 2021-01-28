from django.contrib import admin

# Register your models here.
from .models import Category,UserProfile,Article

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'description']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at']
    search_fields = ['title', 'content']
    
admin.site.register(Category)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Article)