from rest_framework import routers

from organization.viewsets import OrganizationViewSet
from payments.viewsets import PaymentViewSet

router = routers.SimpleRouter()
router.register(r"organization", OrganizationViewSet, basename="organization")
router.register(r"payment", PaymentViewSet, basename="payment")

urlpatterns = router.urls
