from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='obtain_token'), 
    path('refresh/', TokenObtainPairView.as_view(), name='refresh_token'), 
]
