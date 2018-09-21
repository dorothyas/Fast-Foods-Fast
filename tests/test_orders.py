import unittest

from app.orders import OrderList
from app.order import Order


class TestFastFoods(unittest.TestCase):
    def setUp(self):
        self.order_list = OrderList()
        self.sample_order = {
            'foodname' :'beef', 
            'quantity' : 2, 
            'location' : 'ebb'
            }
        self.new_order = {
            'foodname' :'posho', 
            'quantity' : 1, 
            'location' : 'ntinda'
            }

    def test_can_add_order(self):
        self.assertEqual(len(self.order_list.orders), 0)
        self.order_list.add_order(**self.sample_order)
        self.assertEqual(len(self.order_list.orders), 1)

    def test_can_get_all_orders(self):
        self.assertEqual(len(self.order_list.get_all_orders()), 0)
        self.order_list.add_order(**self.sample_order)
        self.order_list.add_order(**self.new_order)
        self.assertEqual(len(self.order_list.get_all_orders()), 2)

    def test_can_get_one_order(self):
        self.assertIsNone(self.order_list.get_one_order(0))
        self.order_list.add_order(**self.sample_order)
        self.assertTrue(self.order_list.get_one_order(1))


    
    

if __name__ == '__main__':
    unittest.main()


    