from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length = 50)
    price = models.FloatField();
    description = models.TextField();
    image = models.ImageField();

    def __str__ (self):
        return self.name + ' : ' + str(self.price)

class Reservation(models.Model):
    name = models.CharField(max_length = 50)
    date = models.DateField(verbose_name = 'Reservation Date');
    time = models.TimeField(verbose_name = 'Reservation Time');
    guests = models.IntegerField(verbose_name = 'Guest Number');
    comment = models.TextField();

    def __str__(self):
        return self.name
