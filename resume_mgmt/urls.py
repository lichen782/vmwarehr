from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from . import views

app_name = 'resume_mgmt'
urlpatterns = [
    url(r'^resume/$', views.success, name='success'),
    url(r'^resume/login/$', auth_views.login, {'template_name': 'resume_mgmt/login.html'}, name="login"),
    url(r'^resume/logout/$', auth_views.logout, {'template_name': 'resume_mgmt/login.html'}, name="logout"),
    url(r'^resume/query/$', views.QueryView.as_view(), name="queryview"),
    url(r'^resume/create/$', views.test, name="create"),
    url(r'^admin/', admin.site.urls),
    url(r'^resume/query/(?P<pk>[0-9]+)$', views.Query.as_view(), name='query'),
    url(r'^resume/edit/(?P<pk>[0-9]+)$', views.edit, name="edit"),
]
