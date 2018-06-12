from django.contrib import admin
from marketplace.models import UserProfileInfo, Posting, Category, Status

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Posting)
admin.site.register(Category)
admin.site.register(Status)
