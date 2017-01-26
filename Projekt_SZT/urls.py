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
from django.conf.urls.static import static
from django.conf import settings
from blog.views import index, show_profile, show_edit_userdata_page, edit_profile, \
    post_modify, post_detail, new_post, add_comment_to_post, comment_approve, comment_remove, blog_categories, \
    show_user_post, show_post_by_categories, post_remove, post_publish

urlpatterns = [

                  url(r'^admin/', admin.site.urls),
                  url(r'^$', index, name='index'),
                  url(r'^accounts/', include('registration.backends.default.urls')),
                  url('', include('social.apps.django_app.urls', namespace='social')),
                  url(r'^show_categories/$', blog_categories, name='blog_categories'),
                  url(r'^post_from_categories/(?P<pk>[0-9]+)/$', show_post_by_categories,
                      name='show_post_by_categories'),
                  url(r'^show_profile/$', show_profile, name='show_profile'),
                  url(r'^new_post_form/$', post_modify, name='post_modify'),
                  url(r'^editprofile/$', show_edit_userdata_page, name='show_edit_userdata_page'),
                  url(r'^apply_form_edit/$', edit_profile, name='edit_profile'),
                  url(r'^tinymce/', include('tinymce.urls')),
                  url(r'^post/(?P<pk>[0-9]+)/$', post_detail, name='post_detail'),
                  url(r'^post/(?P<pk>\d+)/user_post/$', show_user_post, name='show_user_post'),
                  url(r'^post/(?P<pk>[0-9]+)/edit/$', post_modify, name='post_modify'),
                  url(r'^post/new/$', new_post, name='new_post'),
                  url(r'^post/(?P<pk>\d+)/remove/$', post_remove, name='post_remove'),
                  url(r'^post/(?P<pk>\d+)/publish/$', post_publish, name='post_publish'),
                  url(r'^post/(?P<pk>\d+)/comment/$', add_comment_to_post, name='add_comment_to_post'),
                  url(r'^comment/(?P<pk>\d+)/approve/$', comment_approve, name='comment_approve'),
                  url(r'^comment/(?P<pk>\d+)/remove/$', comment_remove, name='comment_remove'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)