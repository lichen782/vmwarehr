from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^resume/$', views.success, name='success'),
    url(r'^resume/login/$', auth_views.login, {'template_name': 'resume_mgmt/login.html'}, name="login"),
    url(r'^resume/logout/$', auth_views.logout, {'template_name': 'resume_mgmt/login.html'}, name="logout"),
    url(r'^resume/create/$', views.create, name="create"),
    url(r'^resume/edit/$', views.edit, name="edit"),
    url(r'^resume/query/$', views.query, name="query"),
    url(r'^admin/', admin.site.urls),
]
