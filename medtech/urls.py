from django.contrib import admin
from django.urls import include, path, re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
   path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
   path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
   path('admin/', admin.site.urls),
   path('api/users/', include('apps.users.urls')),
   path('api/auth/', include('apps.authentication.urls')),
   path('api/inv/', include('apps.investigations.urls')),
]
