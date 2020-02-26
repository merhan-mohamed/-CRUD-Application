from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey('Author',on_delete=models.CASCADE)
    image = models.ImageField()
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project5:post_details', kwargs={'slug':self.slug})

    def get_update_url(self):
        return reverse('project5:posts_update', kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('project5:post_delete', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super(Post, self).save(*args, **kwargs)






class Author(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.EmailField()
    cellphone = models.IntegerField()

    def __str__(self):
        return self.user.username