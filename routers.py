from rest_framework import routers

from organization.viewsets import OrganizationViewSet

router = routers.SimpleRouter()
router.register(r'organization', OrganizationViewSet)

urlpatterns = router.urls
