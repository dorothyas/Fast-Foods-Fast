import unittest

from views import app
from flask import json



class TestFastFoods(unittest.TestCase):
    def setUp(self):
        self.app= app
        self.client = self.app.test_client()
        self.order1 = dict(FoodName='beef', Quantity=3, Location='Ebb')
        self.order2 = dict(FoodName='chips', Quantity=4, Location='kla')
         
      
    def test_can_add_order(self):
        res = self.client.post('/v1/orders', json=self.order1, content_type='application/json')
        self.assertEqual(res.status_code, 200)

    '''def test_cant_add_empty_order(self):
        res = self.client.post('/v1/orders', json=dict(FoodName='', Quantity=1, location='ntinda'), content_type='application/json')
        self.assertEqual(res.status_code, 400)'''
    
    def test_can_get_all_orders(self):
        res = self.client.get('/v1/orders')
        self.assertEqual(res.status_code, 200)

        res_1 = self.client.get('/v1/orders/f')
        self.assertEqual(res_1.status_code, 404)

    def test_can_get_one_order(self):
        res = self.client.get('/v1/orders/1')
        self.assertEqual(res.status_code, 200)

    def test_can_edit_order(self):
        self.client.post('/v1/orders', json=self.order1, 
         content_type='application/json')
        self.client.post('/v1/orders', json=self.order2, content_type='application/json') 
        self.client.get ('/v1/orders/1')
        res = self.client.put('v1/orders/1', json=self.order2, content_type='application/json')
        self.assertEqual(res.status_code, 200)
        


if __name__ == '__main__':
    unittest.main()
