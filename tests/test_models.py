from django.test import TestCase
from restaurant.models import MenuItem


class MenuItemTestCase(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(
            title = 'IceCream',
            price = 80,
            inventory = 50
        )
        self.assertEqual(str(item), 'IceCream: 80')