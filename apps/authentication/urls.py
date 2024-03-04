from django.urls import path
from apps.authentication.apis import UserLogoutAPi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('v1/authenticate', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/logout', UserLogoutAPi.as_view(), name='auth_logout'),
]
