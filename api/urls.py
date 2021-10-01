from django.urls import path

from rest_framework import routers

from .viewsets import CartViewSet
from .views import AuthCheck, LoginView


router = routers.SimpleRouter()
router.register(r'carts', CartViewSet)

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('auth-check/', AuthCheck.as_view())
]

urlpatterns += router.urls
