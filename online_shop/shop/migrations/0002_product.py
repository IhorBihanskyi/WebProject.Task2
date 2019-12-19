# Generated by Django 2.2.8 on 2019-12-15 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Name')),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d/', verbose_name='Product image')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('stock', models.PositiveIntegerField(verbose_name='In stock')),
                ('available', models.BooleanField(default=True, verbose_name='Available')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='shop.Category', verbose_name='Category')),
            ],
            options={
                'index_together': {('id', 'slug')},
                'ordering': ['name'],
            },
        ),
    ]
