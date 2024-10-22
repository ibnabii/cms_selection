from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

wagtail_urls = [
    path("cms/", include("wagtail.admin.urls")),  # Wagtail admin URLs
    path("documents/", include("wagtail.documents.urls")),  # Wagtail document URLs
    path("pages/", include("wagtail.urls")),
]

urlpatterns = i18n_patterns(
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path("admin/", admin.site.urls),
    path("django-cms/", include("cms.urls")),
    path("wagtail/", include(wagtail_urls)),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
