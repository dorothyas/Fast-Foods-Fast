import unittest

from api import app
from flask import json



class TestFastFoods(unittest.TestCase):
    def setUp(self):
        self.app= app
        self.client = self.app.test_client()
      
    def test_can_add_order(self):
        res = self.client.post('/v1/orders', data=json.dumps(
            dict(FoodName='beef', Quantity=3, location='Ebb')), content_type='application/json')
        self.assertEqual(res.status_code, 200)

        res = self.client.post('/v1/orders', data=json.dumps(
            dict(FoodName='', Quantity=1, location='ntinda')), content_type='application/json')
        self.assertEqual(res.status_code, 400)
    
    def test_can_get_all_orders(self):
        res = self.client.get('/v1/orders')
        self.assertEqual(res.status_code, 200)

        res_1 = self.client.get('/v1/orders/f')
        self.assertEqual(res_1.status_code, 404)

    def test_can_get_one_order(self):
        res = self.client.get('/v1/orders/1')
        self.assertEqual(res.status_code, 200)

    def test_can_edit_order(self):
        res = self.client.put('v1/orders/1', content_type='application/json',data=json.dumps(
            dict(order_status="success")))
        self.assertEqual(res.status_code, 201)    


if __name__ == '__main__':
    unittest.main()
