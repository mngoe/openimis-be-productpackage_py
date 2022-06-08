from django.db import models
from product import models as product_models
from productpackage import models as productpackage_models
from medical import models as medical_models

# Create your models here.
class ProductPackage(models.Model):
    id = models.AutoField( primary_key=True)
    PackageType = models.CharField(db_column="PackageType", max_length=20, blank=True, null=True)
    PackageName = models.CharField(db_column="PackageName", max_length=100, blank=True, null=True)
    PackageDate = models.DateTimeField(db_column="PackageDate", blank=True, null=True)
    PackagePrice = models.DecimalField(db_column="PackagePrice", max_digits=18, decimal_places=2,  blank=True, null=True)
    PackageCheckBox = models.BooleanField(default= True)


    class Meta:
        managed = True
        db_table ='tblProducPackage'


class ProductContainedPackage(models.Model):
    idPCP = models.AutoField( primary_key=True)
    productId = models.ForeignKey(product_models.Product, models.DO_NOTHING, db_column="ProductId")
    productpackageId = models.ForeignKey(productpackage_models.ProductPackage, models.DO_NOTHING, db_column="id")
    PCPQuantity = models.IntegerField(db_column="PCPQuantity", blank=True, null=True)
    PCPDate = models.DateTimeField(db_column="PackageDate", blank=True, null=True)
    PCPPrice = models.DecimalField(db_column="PackagePrice", max_digits=18, decimal_places=2,  blank=True, null=True)


    class Meta:
        managed = True
        db_table ='tblProductContainedPackage'


class ServiceContainedPackage(models.Model):
    idSCP = models.AutoField( primary_key=True)
    product_packageId = models.ForeignKey(productpackage_models.ProductPackage, models.DO_NOTHING, db_column="id")
    medical_serviceId = models.ForeignKey(medical_models.Service, models.DO_NOTHING, db_column="ServiceID")
    SCPQuantity = models.IntegerField(db_column="PCPQuantity", blank=True, null=True)
    SCPDate = models.DateTimeField(db_column="PackageDate", blank=True, null=True)
    SCPPrice = models.DecimalField(db_column="PackagePrice", max_digits=18, decimal_places=2, blank=True, null=True)


    class Meta:
        managed = True
        db_table ='tblServiceContainedPackage'

