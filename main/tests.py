from django.test import TestCase, Client
from main.models import Item
from django.db import models

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
    
    def test_instance_model(self):
        #Create instance of Item
        test_model = Item(name="Soto Betawi", amount=3, price=25000, description="Kuah menggunakan susu", category="Main Course", origin="Betawi")

        #Verify that the attributes match what set before
        self.assertEqual(test_model.name, "Soto Betawi")
        self.assertEqual(test_model.amount, 3)
        self.assertEqual(test_model.price, 25000)
        self.assertEqual(test_model.description, "Kuah menggunakan susu")
        self.assertEqual(test_model.category, "Main Course")
        self.assertEqual(test_model.origin, "Betawi")
    
    def test_save_and_retreive_data(self):
        #Create instance of Item
        test_model = Item(name="Soto Betawi", amount=3, price=25000, description="Kuah menggunakan susu", category="Main Course", origin="Betawi")

        #Save it to database
        test_model.save()

        #Retrieve the object from the database
        retrieved_model = Item.objects.get(name="Soto Betawi")

        #Verify that the attributes match what retrieved before
        self.assertEqual(retrieved_model.name, "Soto Betawi")
        self.assertEqual(retrieved_model.amount, 3)
        self.assertEqual(retrieved_model.price, 25000)
        self.assertEqual(retrieved_model.description, "Kuah menggunakan susu")
        self.assertEqual(retrieved_model.category, "Main Course")
        self.assertEqual(retrieved_model.origin, "Betawi")
    

