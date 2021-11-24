from flask import render_template
from app import app
from models.order_list import orders


@app.route('/orders')
def index():
    return render_template('index.html',title='Order List', orders=orders)

@app.route('/orders/<index>')
def order(index):
    order_num = int(index)
    return render_template('order.html',title='Order', order=orders[order_num])