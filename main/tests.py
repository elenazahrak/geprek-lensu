from django.test import TestCase
from django.test import TestCase, Client
from main.models import Product

# Create your tests here.
class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')


class bonusTest(TestCase):
    def setUp(self):
        self.paket_satu = Product.objects.create(menu="Paket Ayam Geprek 1 (Level 1-5)", price=15000, stock=20, description="Ayam Geprek (Level 1-5) + Nasi")
        self.paket_dua = Product.objects.create(menu="Paket Ayam Geprek 3 (Pedas Nangis)", price=21000, stock=5, description="Ayam Geprek (Level MAX) + Nasi + Es Teh Manis")

    def add_stock_test(self):
        nama_menu = self.paket_satu.menu
        stock = self.paket_satu.stock
        stock_added = 3
        stock += stock_added
        self.assertEqual(self.add_stock(self, stock_added), f"Berhasil menambahkan stock sebanyak {stock_added}. Jumlah stock {nama_menu} saat ini adalah {stock}.")
    
    def order_test(self):
        nama_menu = self.paket_dua.menu
        stock = self.paket_dua.stock
        stock_ordered = 1
        stock -= stock_ordered
        self.assertEqual(self.order(self), f"Pelanggan berhasil memesan {stock_ordered} porsi {nama_menu}! Jumlah stock {nama_menu} saat ini adalah {stock}.")