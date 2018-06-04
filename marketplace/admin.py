from django.contrib import admin
from marketplace.models import UserProfileInfo, Posting, Category

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Posting)
admin.site.register(Category)
