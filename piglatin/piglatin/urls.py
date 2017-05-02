from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'^translate/', views.translate, name='translate'),
    url(r'^about/', views.about, name='about'),
]
