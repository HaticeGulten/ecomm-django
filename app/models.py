from django.db import models

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