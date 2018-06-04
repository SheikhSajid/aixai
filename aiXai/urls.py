"""aiXai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

from dataset_uploader import views as du_views
from marketplace import views as mp_views


urlpatterns = [
    url(r'^$', mp_views.index, name='index'),
    url(r'^upload/', du_views.index, name='upload'),
    url(r'^submissions/', du_views.submissions, name='submissions'),
    url(r'^logout/', mp_views.user_logout, name='logout'),
    url(r'^login/', mp_views.user_login, name='login'),
    url(r'^admin/', admin.site.urls),
    url(r'^user/(?P<username>\w+)/', mp_views.user_profile),
    url(r'^dataset_uploader/', include('dataset_uploader.urls')),
    url(r'^marketplace/', include('marketplace.urls'))
]
