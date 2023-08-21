from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.views import MenuItemSerializer


class MenuItemTestCase(TestCase):
    def setUp(self):
        self.item = MenuItem.objects.create(
            title = 'IceCream',
            price = 80.55,
            inventory = 50
        )
        self.serializer = MenuItemSerializer(instance=self.item)

    def test_model_serializer(self):
        serializer_data = self.serializer.data
        self.assertEqual(str(self.item), f'{serializer_data["title"]}: {serializer_data["price"]}')