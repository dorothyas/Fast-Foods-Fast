from app.order import Order


class OrderList:
    def __init__(self):
        self.orders = {}
        self.orders_count = {}
        self.order_id = len(self.orders)+1

    def add_order(self, foodname, quantity, location):
        
        if foodname in self.orders:
            self.orders_count[foodname] += 1
        else:
            self.orders_count[foodname] = 1
            self.orders[foodname] = Order(foodname, quantity, location, self.order_id )
        return self.orders

    def get_all_orders(self):
        return list(self.orders.keys())

    def get_one_order(self, order_id):
        return self.orders[self.order_id]

    def edit_order(self, foodname, quantity, location):
        if foodname not in self.orders:
            return
