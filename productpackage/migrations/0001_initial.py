# Generated by Django 3.0.14 on 2022-06-04 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0002_productmutation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productType', models.CharField(blank=True, db_column='productType', max_length=100, null=True)),
                ('productId', models.ForeignKey(db_column='ProductId', on_delete=django.db.models.deletion.DO_NOTHING, to='product.Product')),
            ],
        ),
    ]
