# Generated by Django 4.1.2 on 2023-04-27 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('composition', models.TextField(default='')),
                ('prodapp', models.TextField(default='')),
                ('category', models.CharField(choices=[('PP', 'Pasta-Napolitano'), ('PL', 'Prawnlin-Guine'), ('RJ', 'RigatoniAll-Julio'), ('RD', 'Rigatonia-Dolcevita'), ('SB', 'SpagettiAlla-Bolognese'), ('SL', 'SpagettiAlla-Carbonara'), ('SM', 'Spagetti-Marina'), ('LZ', 'Lazagnea-Alforno')], max_length=2)),
                ('product_image', models.ImageField(upload_to='product')),
            ],
        ),
    ]