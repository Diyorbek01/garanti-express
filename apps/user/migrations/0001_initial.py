# Generated by Django 4.1.3 on 2022-11-10 10:11

from django.db import migrations, models
import phonenumber_field.modelfields
import user.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('legal_name', models.CharField(max_length=255, unique=True)),
                ('brand_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('status', models.CharField(choices=[('seller', 'seller'), ('customer', 'customer')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('admin', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('superuser', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'user',
            },
            managers=[
                ('objects', user.manager.CustomUserManager()),
            ],
        ),
    ]
