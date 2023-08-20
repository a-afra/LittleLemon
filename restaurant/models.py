from django.db import models

# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    guest_number = models.IntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return self.title