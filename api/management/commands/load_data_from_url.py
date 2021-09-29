import csv
import requests

from django.core.management.base import BaseCommand

from api.models import Item, Cart


class Command(BaseCommand):
    help = 'specify model in --model argument and enter path to csv file'

    def add_arguments(self, parser):
        parser.add_argument(
            '-m',
            '--model',
            choices=['Item', 'Cart'],
            required=True,
            help='select model name'
        )
        parser.add_argument(
            '-f',
            '--format',
            choices=['json', 'csv'],
            required=True,
            help='select data format'
        )
        parser.add_argument(
            'url',
        )

    def handle(self, *args, **options):
        if options['model'] == 'Cart':
            if options['format'] == 'json':
                self.create_carts_from_json(options['url'])
            else:
                self.print_format_error(options)
        elif options['model'] == 'Item':
            if options['format'] == 'csv':
                self.create_items_from_csv(options['url'])
            else:
                self.print_format_error(options)

    def print_format_error(self, options):
        print('Can not create {0} objects from {1} format'.format(options['model'], options['format']))

    def create_items_from_csv(self, url):
        response = requests.get(url)
        data = response.content.decode('utf-8').splitlines()
        records = csv.DictReader(data, delimiter=',')
        items = []
        for row in records:
            item_kwargs = {
                'id': row['id'],
                'name': row['item_name'],
                'barcode': row['barcode'],
                'price': row['price'],
            }
            if row['promotion']:
                item_kwargs['discount'] = row['promotion']
            items.append(Item(**item_kwargs))
        Item.objects.bulk_create(items)

    def create_carts_from_json(self, url):
        response = requests.get(url)
        data = response.json()
        for row in data:
            cart = Cart.objects.create(
                id=row['id'],
                app_mode=row['app_mode'].lower().replace(' ', '_'),
                cart_status=row['cart_status'].lower(),
                created_at=row['created_at']
            )
            cart.save()
            cart.items.set(row['item_id'])
            cart.save()
