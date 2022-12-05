# Generated by Django 4.1.3 on 2022-11-10 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product_category', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256)),
                ('code', models.PositiveIntegerField(unique=True)),
                ('is_delete', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('model', models.CharField(max_length=256)),
                ('barcode', models.PositiveIntegerField(unique=True)),
                ('manufacturer', models.CharField(max_length=256)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('canceled', 'Canceled'), ('deleted', 'Deleted')], max_length=10)),
                ('published_at', models.DateTimeField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('unisex', 'Unisex'), ('kids', 'Kids')], max_length=10)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product_category.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product_category.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('good_kdv', models.PositiveIntegerField()),
                ('stock_code', models.PositiveIntegerField(unique=True)),
                ('amount', models.PositiveIntegerField()),
                ('is_discount', models.BooleanField(default=False)),
                ('market_price', models.PositiveIntegerField()),
                ('gr_price', models.PositiveIntegerField()),
                ('discount', models.PositiveIntegerField()),
                ('comission', models.PositiveIntegerField()),
                ('weight', models.PositiveIntegerField()),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_stocks', to='product.color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_stocks', to='product.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='products/images/')),
                ('video', models.FileField(upload_to='products/videos/')),
                ('is_image', models.BooleanField(default=True)),
                ('product_stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medias', to='product.productstock')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
