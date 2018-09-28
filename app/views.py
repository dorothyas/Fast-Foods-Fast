from flask import Flask, jsonify, request 
app = Flask(__name__)


orders = [] 

@app.route('/v1/orders',methods=['POST'])
def addOrder():
    userOrder = {'FoodName': request.json['FoodName'], 
                'Quantity': request.json['Quantity'], 
                'Location': request.json['Location'],
                'orderId' : len(orders) +1}

    orders.append(userOrder)
    return jsonify({'orders': orders})

@app.route('/v1/orders',methods=['GET'])
def allOrders():
    return jsonify({'orders' : orders})

@app.route('/v1/orders/<int:orderId>',methods=['GET'])
def oneOrder(orderId):
    order = [order for order in orders if order ['orderId'] == orderId] 
    return jsonify({'orders' : order})


@app.route('/v1/orders/<int:orderId>',methods=['PUT'])
def edit(orderId):
    order1 = [order1 for order1 in orders if order1['orderId'] == orderId]
    order1[0]['FoodName'] = request.json['FoodName']
    order1[0]['Quantity']= request.json['Quantity']
    order1[0]['Location']= request.json['Location']
    return jsonify({'order': order1})



