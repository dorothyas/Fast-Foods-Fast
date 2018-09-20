import unittest

from app.orders import OrderList


class TestFastFoods(unittest.TestCase):
    def setUp(self):
        self.order_list = OrderList()
        self.sample_order = dict(
            foodname= 'beef', 
            quantity= 2, 
            location= 'ebb'
        )   
    def test_can_add_order(self):
        self.assertEqual(len(self.order_list.orders), 0)
        self.order_list.add_order(**self.sample_order)
        self.assertEqual(len(self.order_list.orders), 1)

    def test_can_get_all_orders(self):
        new = self.sample_order
        self.assertEqual(len(new),len(self.sample_order))
    
    

if __name__ == '__main__':
    unittest.main()
    