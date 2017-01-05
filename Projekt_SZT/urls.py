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
from blog.views import index, show_profile, redirect_to_new_post_page, show_edit_userdata_page, edit_profile

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^show_profile/$', show_profile, name='show_profile'),
    url(r'^new_post/$', redirect_to_new_post_page, name='redirect_to_new_post_page'),
    url(r'^editprofile/$', show_edit_userdata_page, name='show_edit_userdata_page'),
    url(r'^apply_form_edit/$', edit_profile, name='edit_profile'),

]
