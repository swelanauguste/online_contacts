from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("contacts.urls", namespace="contacts")),
    path("admin/", admin.site.urls),
]
