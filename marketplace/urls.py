from django.conf.urls import url
from marketplace import views

# TEMPLATE TAGGING
app_name = 'marketplace'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^posting/(?P<post_id>\d+)/', views.post_description, name='posting_description'),
    url(r'^status/', views.user_profile, name='status'),
    url(r'^(?P<category>.+)/', views.posts_of_category, name='category'),
]
