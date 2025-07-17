import unittest
from models import Order, MenuItem
from exceptoins import InvalidQuantityException, ItemNotInOrderException

class TestOrder(unittest.TestCase):

    def setUp(self) -> None:
        self.phone = MenuItem('phone', 650)
        self.headset = MenuItem('headset', 250)
        self.watch = MenuItem('watch', 150)
        self.order = Order()


    def tearDown(self) -> None:
        self.order.clear_order()

    def test_add_item(self):
        list_order = self.order.add_item(self.phone, 25)
        list_order = self.order.add_item(self.headset, 35)
        list_order = self.order.add_item(self.watch, 45)

        self.assertEqual(list_order, {
            'phone': (25, 650),
            'headset': (35, 250),
            'watch': (45,150)
        }
                         )

    def test_exception_add(self):
        with self.assertRaises(InvalidQuantityException):
            self.order.add_item(self.phone, 0)


    def test_remove_item(self):
        list_order = self.order.add_item(self.phone, 25)
        list_order = self.order.add_item(self.headset, 35)
        list_order = self.order.add_item(self.watch, 45)
        list_order = self.order.remove_item(self.phone)

        self.assertEqual(list_order, {
            'headset': (35, 250),
            'watch': (45,150)
        }

        )


    def test_exception_remove(self):
        list_order = self.order.add_item(self.watch, 45)

        with self.assertRaises(ItemNotInOrderException):
            list_order = self.order.remove_item(self.phone)


