from rest_framework import routers

from .viewsets import CartViewSet

router = routers.SimpleRouter()
router.register(r'cart', CartViewSet)
urlpatterns = router.urls