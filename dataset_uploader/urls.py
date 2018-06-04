from django.conf.urls import url
from dataset_uploader import views

app_name = 'dataset_uploader'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new_submission/', views.new_submission, name='new submission')
]