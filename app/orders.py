from app.order import Order


class OrderList:
    def __init__(self):
        self.orders = dict()
        self.orders_count = dict()

    def add_order(self, foodname, quantity, location):
        
        if foodname in self.orders:
            self.orders_count[foodname] += 1
        else:
            self.orders_count[foodname] = 1
            self.orders[foodname] = Order(foodname, quantity, location )
        return self.orders

    def get_all_orders(self):
        return list(self.orders.keys())