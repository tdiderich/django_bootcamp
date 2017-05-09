from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^create/', views.create, name="create"),
    url(r'^(?P<pk>[0-9]+)/up_vote', views.up_vote, name="up_vote"),
    url(r'^(?P<pk>[0-9]+)/down_vote', views.down_vote, name="down_vote"),
    url(r'^(?P<username>\w+)/$', views.profile, name='profile')
]
