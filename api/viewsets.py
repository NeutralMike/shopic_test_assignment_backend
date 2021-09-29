from django.db.models import Count, Sum, F

from rest_framework.viewsets import GenericViewSet, mixins

from .serializers import CartSerializer
from .models import Cart


class CartViewSet(GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        return self.queryset.prefetch_related('items').annotate(
            items_count=Count('items'),
            total_price_without_discount=Sum('items__price'),
            total_discount=Sum(F('items__price') * (100 - F('items__discount') / 100)),
            total_price=F('total_price_without_discount') - F('total_discount')
        )