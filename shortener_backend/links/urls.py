from django.urls import include, path
from rest_framework.routers import DefaultRouter

from links.views import LinkViewSet, RedirectView

router = DefaultRouter()
router.register(r"links", LinkViewSet, basename="links")

urlpatterns = [
    path("api/", include(router.urls)),
    path("<str:shortened_url_path>/", RedirectView.as_view()),
]
