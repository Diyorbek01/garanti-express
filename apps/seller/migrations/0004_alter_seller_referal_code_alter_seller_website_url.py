# Generated by Django 4.1.3 on 2022-11-10 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_alter_city_region_alter_region_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='referal_code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='website_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
