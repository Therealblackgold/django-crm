from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('members/', include('accounts.urls')),
    path('christian-admin/', include('app_admin.urls')),
    path('summernote/', include('django_summernote.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
