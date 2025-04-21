
from django.contrib import admin
from django.urls import path, include, re_path
from .consumer import NotificationConsumer

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("researcher.urls"))
]


websocket_urlpatterns = [
    re_path('ws/notifications', NotificationConsumer.as_asgi()),
]

