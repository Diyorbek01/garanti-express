# Generated by Django 4.1.3 on 2022-11-25 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0009_remove_seller_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='region',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='seller.region'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='region',
            name='country',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='regions', to='seller.country'),
            preserve_default=False,
        ),
    ]
