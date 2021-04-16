from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.




class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'


    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=120)
    slug= models.SlugField(max_length=120)

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=255)
    feature_image = models.ImageField(upload_to="news_feature_image")
    description = models.TextField()
    views = models.IntegerField(default=0)
    address = models.CharField(max_length=155, blank=True, null=True)
    category = models.ForeignKey(Category, related_name="news", on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, blank=True, null=True, on_delete=models.SET_NULL)
    author = models.CharField(max_length=120, default="admin")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add = True)
    is_published = models.BooleanField(default=True)
    is_trending = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)


    def get_absolute_url(self):
        return reverse('blog-single', args=[self.id])


    def __str__(self):
        return self.title


class Comment(models.Model):
    comment_text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank=True)
    post = models.ForeignKey(News, on_delete=models.CASCADE)
    is_parent = models.ForeignKey('self',blank=True, null=True, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    upated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.comment_text[:20] + "by " + str( self.author)

class Advertise(models.Model):
    title = models.CharField(max_length=125)
    link = models.TextField(blank=True, null=True)
    featured_image = models.ImageField(upload_to="ad_featured_image", blank=True, null=True)
    featured_vertical_image = models.ImageField(upload_to="ad_featured_image", blank=True, null=True)


    def __str__(self):
        return self.title


class TrendingNow(models.Model):
    title = models.CharField(max_length=300)


    def __str__(self):
        return self.title