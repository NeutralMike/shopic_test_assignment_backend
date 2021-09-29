from django.db.models import Count, Sum, F, Value, DecimalField
from django.db.models.functions import Coalesce

from rest_framework.viewsets import GenericViewSet, mixins

from .serializers import CartListSerializer, CartDetailSerializer
from .models import Cart


class CartViewSet(GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    queryset = Cart.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CartDetailSerializer
        return CartListSerializer

    def get_queryset(self):
        return self.queryset.prefetch_related('items')\
            .annotate(
                items_count=Count('items'),
                total_price_without_discount=Coalesce(Sum('items__price'), Value(0), output_field=DecimalField()),
                total_discount=Coalesce(
                    Sum(F('items__discount') * F('items__price')/100),
                    Value(0),
                    output_field=DecimalField()
                ),
                total_price=Coalesce(
                    F('total_price_without_discount') - F('total_discount'),
                    Value(0),
                    output_field=DecimalField()
                )
            )
