#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    bakeries = [bakery.to_dict() for bakery in Bakery.query.all()]
    response = make_response(bakeries, 200, {"Content-Type": "application/json"})
    return response

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    backery = Bakery.query.filter(Bakery.id == id).first()
    backery_dict = backery.to_dict()
    response = make_response(backery_dict, 200, {"Content-Type": "application/json"})
    return response

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    backed_goods = BakedGood.query.order_by(BakedGood.price.desc()).all()
    baked_goods_list = [baked_good.to_dict() for baked_good in backed_goods]
    response = make_response(baked_goods_list, 200, {"Content-Type": "application/json"})
    return response

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    backed_goods = BakedGood.query.order_by(BakedGood.price.desc()).limit(1).first()
    backed_goods_dict = backed_goods.to_dict()
    response = make_response(backed_goods_dict, 200)
    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
