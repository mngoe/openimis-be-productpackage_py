# Generated by Django 3.0.14 on 2022-06-13 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medical', '0003_mutations'),
        ('product', '0002_productmutation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPackage',
            fields=[
                ('IdPackage', models.AutoField(db_column='PackageID', primary_key=True, serialize=False)),
                ('PackageType', models.CharField(blank=True, db_column='PackageType', max_length=20, null=True)),
                ('PackageName', models.CharField(blank=True, db_column='PackageName', max_length=100, null=True)),
                ('PackageDate', models.DateTimeField(blank=True, db_column='PackageDate', null=True)),
                ('PackagePrice', models.DecimalField(blank=True, db_column='PackagePrice', decimal_places=2, max_digits=18, null=True)),
                ('PackageCheckBox', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'tblProducPackage',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ServiceContainedPackage',
            fields=[
                ('idSCP', models.AutoField(primary_key=True, serialize=False)),
                ('SCPQuantity', models.IntegerField(blank=True, db_column='PCPQuantity', null=True)),
                ('SCPDate', models.DateTimeField(blank=True, db_column='PackageDate', null=True)),
                ('SCPPrice', models.DecimalField(blank=True, db_column='PackagePrice', decimal_places=2, max_digits=18, null=True)),
                ('medical_serviceId', models.ForeignKey(db_column='ServiceID', on_delete=django.db.models.deletion.DO_NOTHING, to='medical.Service')),
                ('product_packageId', models.ForeignKey(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, to='productpackage.ProductPackage')),
            ],
            options={
                'db_table': 'tblServiceContainedPackage',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProductContainedPackage',
            fields=[
                ('idPCP', models.AutoField(primary_key=True, serialize=False)),
                ('PCPQuantity', models.IntegerField(blank=True, db_column='PCPQuantity', null=True)),
                ('PCPDate', models.DateTimeField(blank=True, db_column='PackageDate', null=True)),
                ('PCPPrice', models.DecimalField(blank=True, db_column='PackagePrice', decimal_places=2, max_digits=18, null=True)),
                ('productId', models.ForeignKey(db_column='ProductId', on_delete=django.db.models.deletion.DO_NOTHING, to='product.Product')),
                ('productpackageId', models.ForeignKey(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, to='productpackage.ProductPackage')),
            ],
            options={
                'db_table': 'tblProductContainedPackage',
                'managed': True,
            },
        ),
    ]
