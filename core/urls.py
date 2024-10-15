from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('dashboard/', admin.site.urls),
    path('v1.0/house/', include('apps.house.urls')),
    path('v1.0/main/', include('apps.main.urls')),
    path('v2/auth/', include('apps.accounts.urls')),
    path('docs/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)