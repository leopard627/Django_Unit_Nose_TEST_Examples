from django.test import Client
from .models import Fruit
import nose.tools as nt


class TestFruit(object):
    def setup(self):
        self.fruit = Fruit()
        self.fruit.set_name("Papaya")
        self.fruit.set_color("orange")

    def test_color(self):
        nt.assert_equal(self.fruit.name, "Papaya")
        nt.assert_equal(self.fruit.color, "orange")

    def test_yumminess(self):
        nt.assert_true(self.fruit.is_yummy())

    def test_color_change(self):
        self.fruit.become_brown()
        nt.assert_equal(self.fruit.color, "brown")

    def teardown(self):
        self.fruit.disappear()


class TestFruitView(object):

    def setup(self):
        self.client = Client()

    def test_product_index(self):
        response = self.client.get("/fruits/")
        nt.assert_equal(response.content, b"The index")

    def test_product_show(self):
        response = self.client.get("/fruits/papaya")
        nt.assert_equal(response.content, b"Show the papaya page")

    def test_product_add(self):
        response = self.client.get("/fruits/add")
        nt.assert_equal(response.content, b"Add a fruit")

