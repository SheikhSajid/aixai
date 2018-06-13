from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)

    about = models.CharField(max_length=500, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pictures', blank=True)

    def __str__(self):
        return self.user.username


class Posting(models.Model):
    user = models.ForeignKey(UserProfileInfo)

    price = models.FloatField(default=1)

    def __str__(self):
        return "{} {}".format(self.submission.name, str(self.price))


class Category(models.Model):
    name = models.CharField(max_length=100)
    postings = models.ManyToManyField(Posting)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Status(models.Model):
    body = models.CharField(max_length=240)
    user_profile = models.ForeignKey(UserProfileInfo, related_name='statuses')
    created_at = models.DateTimeField(auto_now_add=True)

    likes = models.ManyToManyField(UserProfileInfo, related_name='likers')
    no_of_likes = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'statuses'

    def __str__(self):
        return self.body
