from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    path('api/', include('dashboard.api.urls', namespace='api')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

