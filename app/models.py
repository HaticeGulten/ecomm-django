from django.db import models
from django.contrib.auth.models import User

STATE_CHOICES = (
    ('Adana', 'Adana'),
    ('Adıyaman', 'Adıyaman'),
    ('Afyonkarahisar', 'Afyonkarahisar'),
    ('Ankara', 'Ankara'),
    ('Antalya', 'Antalya'),
    ('Aydın', 'Aydın'),
    ('Balıkesir', 'Balıkesir'),
    ('Bursa', 'Bursa'),
    ('Çanakkale', 'Çanakkale'),
    ('Denizli', 'Denizli'),
    ('Edirne', 'Edirne'),
    ('Eskişehir', 'Eskişehir'),
    ('Gaziantep', 'Gaziantep'),
    ('Hatay', 'Hatay'),
    ('Isparta', 'Isparta'),
    ('İstanbul', 'İstanbul'),
    ('İzmir', 'İzmir'),
    ('Kahramanmaraş', 'Kahramanmaraş'),
    ('Kocaeli', 'Kocaeli'),
    ('Konya', 'Konya'),
    ('Kütahya', 'Kütahya'),
    ('Manisa', 'Manisa'),
    ('Mersin', 'Mersin'),
    ('Muğla', 'Muğla'),
    ('Sakarya', 'Sakarya'),
    ('Samsun', 'Samsun'),
    ('Sivas', 'Sivas'),
    ('Trabzon', 'Trabzon'),
    ('Uşak', 'Uşak'),
    ('Zonguldak', 'Zonguldak'),
)

CATEGORY_CHOICES=(
    ('PN', 'Pasta-Napolitano'),
    ('PL', 'Prawn-Linguine'),
    ('RJ', 'RigatoniAll-Julio'),
    ('RD', 'Rigatonia-Dolcevita'),
    ('SB', 'SpagettiAlla-Bolognese'),
    ('SC', 'SpagettiAlla-Carbonara'),
    ('SM', 'Spagetti-Marina'),
    ('LZ', 'Lazagnea-Alforno'),    
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default="")
    prodapp = models.TextField(default="")
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title
    
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)
    def __str__(self):
        return self.name
