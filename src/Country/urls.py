from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.overview, name='overview'),
    path('api/', include('api.urls'), name='api-urls'),
    path('security/', include('security.urls'), name='api-urls'),
    path('admin/', admin.site.urls),
]
