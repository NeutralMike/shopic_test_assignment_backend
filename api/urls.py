from rest_framework import routers

from .viewsets import CartViewSet

router = routers.SimpleRouter()
router.register(r'carts', CartViewSet)
urlpatterns = router.urls