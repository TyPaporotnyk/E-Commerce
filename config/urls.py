from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("jet/", include("jet.urls", "jet")),  # Django JET URLS
    path("admin/", admin.site.urls),
    path("api/v1/", include("src.routes")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
