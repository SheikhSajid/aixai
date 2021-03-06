from django.db import models
from marketplace.models import UserProfileInfo, Posting


# Create your models here.
class Submission(models.Model):
    user_profile = models.ForeignKey(UserProfileInfo, on_delete=models.SET_NULL, null=True)
    posting = models.OneToOneField(Posting, on_delete=models.SET_NULL, null=True, blank=True)

    data_type = models.CharField(max_length=264)
    no_of_entries = models.IntegerField(default=0)
    name = models.CharField(max_length=264)
    date_of_submission = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=264, default="Under Progress")
    filename = models.CharField(max_length=120, null=True, blank=True)

    increase_by = models.CharField(max_length=3, default='1X')

    def __str__(self):
        return "%s %s %s" % (self.name, self.data_type, self.no_of_entries)
