from django.db import models


class Item(models.Model):

    name = models.CharField(max_length=255, db_index=True)
    barcode = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.PositiveSmallIntegerField(default=0)


class Cart(models.Model):

    FRICTIONLESS = 'frictionless'
    CART_WATCH = 'cart_watch'
    APP_MODE_CHOICES = [
        (FRICTIONLESS, 'Frictionless'),
        (CART_WATCH, 'Cart Watch'),
    ]

    ACTIVE = 'active'
    ABANDONED = 'abandoned'
    COMPLETED = 'completed'
    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (ABANDONED, 'Abandoned'),
        (COMPLETED, 'Completed'),
    ]

    app_mode = models.CharField(choices=APP_MODE_CHOICES, max_length=255)
    status = models.CharField(choices=STATUS_CHOICES, max_length=255)
    created_at = models.DateField()
    items = models.ManyToManyField(Item)
