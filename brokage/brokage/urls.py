from django.contrib import admin
from .views import index
from django.urls import path, include

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls"))
]
