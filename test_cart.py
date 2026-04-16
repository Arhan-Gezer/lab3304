from cart import ShoppingCart
import unittest

class TestAddFunction(unittest.TestCase):
    def test_add_item_quantity_girme_hatası(self):
        cart = ShoppingCart()
        cart.add_item("Elma", 10.0, 3)
        cart.add_item("Elma", 10.0, 4)
        self.assertTrue(cart._items['Elma']['quantity'] == 7)

    def test_apply_discount_indiri_oranı_hatası(self):
        cart = ShoppingCart()
        cart.add_item("Elma",10.0, 4)
        cart.add_item("Armut", 10.0,3)
        cart.apply_discount("SAVE20")
        cart.remove_item("Elma")
        self.assertIsNone(cart._discount)

    def test_apply_discount_subtotal_hatası(self):
        cart = ShoppingCart()
        cart.add_item("Elma",10.0, 5)
        cart.apply_discount("SAVE20")
        self.assertIsNotNone(cart._discount)

    def test_get_item_count(self):
        cart = ShoppingCart()
        cart.add_item("Elma", 10.0, 3)
        cart.add_item("Armut", 5.0, 2)
        self.assertEqual(cart.get_item_count(), 5)

    def get_item_count(self) -> int:
        return sum(item["quantity"] for item in self._items.values())