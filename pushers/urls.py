from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from pusherchat import views

urlpatterns = [
    url(r'^$', views.chat),
    url(r'^admin/', admin.site.urls),
    url(r'^ajax/chat/$', views.broadcast),

]
