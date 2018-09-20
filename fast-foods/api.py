from flask import Flask, jsonify, request 
app = Flask(__name__)


orders =[{"FoodName":"beef","Quantity":5,"Location":"KLA",'orderId' : 1 }]

@app.route('/v1/orders',methods=['POST'])
def addOrder():
    userOrder = {'FoodName': request.json['FoodName'], 
                'Quantity': request.json['Quantity'], 
                'Location': request.json['Location'],
                'orderId' : len(orders) +1}

    orders.append(userOrder)
    return jsonify({'orders': orders})
    

if __name__=='__main__':
     app.run(debug=True)