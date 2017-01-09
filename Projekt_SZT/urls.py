"""Projekt_SZT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from blog.views import index, show_profile, redirect_to_new_post_page, show_edit_userdata_page, edit_profile, \
    post_modify, post_detail, new_post

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^show_profile/$', show_profile, name='show_profile'),
    url(r'^new_post/$', new_post, name='new_post'),
    url(r'^new_post_form/$', post_modify, name='post_modify'),
    url(r'^editprofile/$', show_edit_userdata_page, name='show_edit_userdata_page'),
    url(r'^apply_form_edit/$', edit_profile, name='edit_profile'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^post/(?P<pk>[0-9]+)/$', post_detail, name='post_detail'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', post_modify, name='post_modify'),
    url(r'^post/new/$', new_post, name='new_post'),
]
