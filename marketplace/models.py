from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)

    about = models.CharField(max_length=500)
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
    postings = models.ManyToManyField(Posting, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
