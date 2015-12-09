from flask import request, redirect, flash
from system.core.controller import *

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)
    
        self.load_model('ProductModel')

    def index(self):
        all_items = self.models['ProductModel'].get_all_items()
        return self.load_view('products.html', items=all_items)

    
    def add_form(self):
        return self.load_view('add.html')

    def create(self): 
        item_info = {
        "name" : request.form['name'], 
        "description" : request.form['description'],
        "price" : request.form['price']
        }

        self.models['ProductModel'].add_item(item_info)
        return redirect ('/')

    def show_page(self, id):
        one_item = self.models['ProductModel'].get_item_by_id(id)
        return self.load_view('show.html', item=one_item[0])

    def destroy(self, id):
        self.models['ProductModel'].destroy(id)
        return redirect('/')

    def edit_page(self, id):
        one_item = self.models['ProductModel'].get_item_by_id(id)
        return self.load_view('edit.html', item=one_item[0])

    def update(self, id):
        item_info = {
        "name" : request.form['name'], 
        "description" : request.form['description'],
        "price" : request.form['price']
        }
        
        self.models['ProductModel'].change_item_by_id(item_info, id)
        return redirect ('/')



