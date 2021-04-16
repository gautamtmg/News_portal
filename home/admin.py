from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title', )}


admin.site.register((News, Tag, Comment, Advertise, TrendingNow))