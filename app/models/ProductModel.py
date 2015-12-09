from system.core.model import Model

class ProductModel(Model):
    def __init__(self):
        super(ProductModel, self).__init__()
 
    def add_item(self, info): 
        insert_query = "INSERT INTO items (name, description, price, created_at, updated_at) VALUES ('{}', '{}', '{}', NOW(), NOW())".format(info['name'], info['description'], info['price'])
        return self.db.query_db(insert_query)

    def get_all_items(self):
        get_all_query = "SELECT * FROM items"
        return self.db.query_db(get_all_query)

    def get_item_by_id(self, id):
        get_one_query = "SELECT * FROM items WHERE id = {}".format(id)
        return self.db.query_db(get_one_query)

    def destroy(self, id):
        delete_one_query = "DELETE FROM items WHERE id ={}".format(id)
        return self.db.query_db(delete_one_query)

    def change_item_by_id(self, info, id):
        change_item_query = "UPDATE items SET name='{}', description='{}', price = '{}' WHERE id = {}".format(info['name'], info['description'],info['price'], id)
        return self.db.query_db(change_item_query)
