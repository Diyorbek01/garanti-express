# Generated by Django 4.1.3 on 2022-11-10 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_customuser_is_verified_customuser_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='legal_name',
            field=models.CharField(max_length=255),
        ),
    ]