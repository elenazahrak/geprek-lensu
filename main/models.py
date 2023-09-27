from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    menu = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def add_stock(self, quantity):
        self.stock += quantity
        self.save()
        return f"Berhasil menambahkan stock sebanyak {quantity}. Jumlah stock {self.menu} saat ini adalah {self.stock}."

    def order(self):
        self.stock -= 1
        self.save()
        return f"Pelanggan berhasil memesan 1 porsi {self.menu}! Jumlah stock {self.menu} saat ini adalah {self.stock}."