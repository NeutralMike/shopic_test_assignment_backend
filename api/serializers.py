from rest_framework import serializers

from .models import Item, Cart


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('name', 'barcode', 'price', 'discount')


class CartSerializer(serializers.ModelSerializer):
    items = ItemSerializer()
    items_count = serializers.IntegerField()
    total_price = serializers.DecimalField(decimal_places=2, max_digits=10)
    total_price_without_discount = serializers.DecimalField(decimal_places=2, max_digits=10)
    total_discount = serializers.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        model = Cart
        fields = ('id', 'app_mode', 'status', 'created_at', 'items_count', 'total_price',
                  'total_price_without_discount', 'total_discount')
        read_only_fields = ('items_count', 'total_price', 'total_price_without_discount', 'total_discount')