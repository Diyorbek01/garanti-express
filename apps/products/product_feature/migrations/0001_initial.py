# Generated by Django 4.1.3 on 2022-11-10 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product_category', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='features', to='product_category.department')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FeatureElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256)),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_feature.feature')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_features', to='product_feature.feature')),
                ('feature_elements', models.ManyToManyField(related_name='product_features', to='product_feature.featureelement')),
                ('product_stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_features', to='product.productstock')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
