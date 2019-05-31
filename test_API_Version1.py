import unittest

from app.py import Orders
from app.py import Orderslist

class Orders(unittest.TestCase):
    def test_empty_orders(self):
        self.assertEqual(get(""), "Orders Fetched successfully")

    def test_post_order(self):
        self.assertEqual(post("chips", ""), "The order has been succesfully added")
        
class Orderslist(unittest.TestCase):       

    def test_get_order(self):
        self.assertEqual(get(""), "Order X was fetched successfuly")

    def test_delete_order(self):
        self.assertEqual(delete(""), "The Order was Successfully deleted")
        
    def test_update_order(self):
        self.assertEqual(put("",""), "The Order was Successfully Updated")

if __name__== '__main__':
    unittest.main()
