from django.db import models


class Fruit(models.Model):

    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def set_name(self, name):
        self.name = name

    def set_color(self, color):
        self.color = color

    def is_yummy(self):
        return(True)

    def become_brown(self):
        self.color = "brown"

    def disappear(self):
        self.color = "transparent"
