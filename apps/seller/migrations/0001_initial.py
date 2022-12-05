# Generated by Django 4.1.3 on 2022-11-10 10:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product_category', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('province', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('zip_code', models.PositiveIntegerField()),
                ('status', multiselectfield.db.fields.MultiSelectField(choices=[('billing', 'billing'), ('firm', 'firm'), ('shipping', 'shipping'), ('return_shipping', 'return_shipping')], max_length=64)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BankInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('status', models.CharField(choices=[('financier', 'financier'), ('manager', 'manager')], max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DeliveryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FirmCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('website_url', models.URLField()),
                ('referal_code', models.CharField(max_length=255)),
                ('bank_information_number', models.PositiveIntegerField()),
                ('addresses', models.ManyToManyField(blank=True, related_name='sellers', to='seller.address')),
                ('bank_information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sellers', to='seller.bankinformation')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sellers', to='seller.city')),
                ('finance_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='finance_sellers', to='seller.contact')),
                ('firm_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sellers', to='seller.firmcategory')),
                ('manager_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manager_sellers', to='seller.contact')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sellers', to='product_category.category')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sellers', to='seller.region')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DeliveryTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('delivery_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_times', to='seller.deliverycategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='deliverycategory',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_categories', to='seller.seller'),
        ),
        migrations.AddField(
            model_name='bankinformation',
            name='firm_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_informations', to='seller.firmcategory'),
        ),
    ]
