# Generated by Django 4.1.3 on 2022-11-10 15:13

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('product_category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='gender',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('male', 'male'), ('female', 'female'), ('unisex', 'unisex'), ('kids', 'kids')], max_length=100),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='categories/'),
        ),
    ]
