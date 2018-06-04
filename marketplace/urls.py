from django.conf.urls import url
from marketplace import views

# TEMPLATE TAGGING
app_name = 'marketplace'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<category>\w+)/', views.posts_of_category, name='category'),
    url(r'^posting/(?P<post_id>\d+)/', views.post_description, name='posting_description')
]