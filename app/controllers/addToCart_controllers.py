from flask import Flask, url_for, redirect, Response, request, render_template,session, jsonify
from flask import Flask, render_template
from pymongo import MongoClient
from bson.objectid import ObjectId
from ..models.addToCart_models import Carts_Services





def add_to_cart(product_id):
    product_id = request.form.get('product_id')
    product = list(Carts_Services.Add(product_id))
   

    if product:
        cart_item = {
            'id': str(product['_id']),
            'categories': product['categories'],
            'price': product['price'],
            'colour': product['colour'],
            'description': product['description'],
            'image_url': product['image_url'],
            'quantity': 1
        }

        cart_items = session.get('cart', [])
        for item in cart_items:
            if item['id'] == cart_item['id']:
                item['quantity'] += 1
                break
        else:
            cart_items.append(cart_item)

        session['cart'] = cart_items

    return redirect(url_for('cart'))


def cart():
    cart_items = session.get('cart', [])
    total_price = sum(float(item['price']) * item['quantity'] for item in cart_items)
    cart_count = len(cart_items)
    return render_template('ViewCart.html', cart_items=cart_items, total_price=total_price, cart_count=cart_count)


def update_cart():
    data = request.get_json()
    product_id = data.get('id')
    quantity = int(data.get('value'))

    cart = session.get('cart', [])
    for item in cart:
        if item['id'] == product_id:
            item['quantity'] = quantity
            break

    session['cart'] = cart
    total = round(sum(float(item['price']) * item['quantity'] for item in cart), 2)
    item_price = round(next((float(item['price']) * item['quantity'] for item in cart if item['id'] == product_id), 0), 2)
    return jsonify({'success': True, 'total': total, 'item_price': item_price})


def remove_from_cart():
    item_id = request.form.get('selected_items')
    cart_items = session.get('cart', [])
    cart_items = [item for item in cart_items if item['id'] != item_id]
    session['cart'] = cart_items
    return redirect(url_for('cart'))


def checkout_success():
    session.pop('cart', None)
    return redirect('/checkout_success')


def checkout():
    cart_items = session.get('cart', [])
    total_price = sum(float(item['price']) * item['quantity'] for item in cart_items)
    cart_count = len(cart_items)
    return render_template('Checkout.html', cart_items=cart_items, total_price=total_price, cart_count=cart_count)



def usercheckout():
    cart_items = session.get('cart', [])
    total_price = sum(float(item['price']) * item['quantity'] for item in cart_items)
    # cart_count = len(cart_items)
    return render_template('Checkout.html', total_price=total_price)



def success():
    session.pop('cart', None)
    return render_template('success.html')
