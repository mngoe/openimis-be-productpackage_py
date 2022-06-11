from django.db import models
from product import models as product_models
from productpackage import models as productpackage_models
from medical import models as medical_models

# Create your models here.
class ProductPackage(models.Model):

    productType = models.CharField(db_column="productType", max_length=100, blank=True, null=True)
    productId = models.ForeignKey(
        product_models.Product, models.DO_NOTHING, db_column="ProductId"
    )
    id = models.AutoField( primary_key=True)
    packageType = models.CharField(max_length=20)
    packageName = models.CharField(max_length=100)
    packageCreateDate = models.DateTimeField()
    packagePrice = models.DecimalField(db_column="PackagePrice", max_digits=18, decimal_places=2,  blank=True, null=True)
    packageIsSpecificPriceCheckBox = models.BooleanField(default= True)

    class Meta:
        managed = True
        db_table ='tblProducPackage'


class ProductContainedPackage(models.Model):
    idPCP = models.AutoField( primary_key=True)
    productId = models.ForeignKey(product_models.Product, models.DO_NOTHING, db_column="ProductId")
    productpackageId = models.ForeignKey(productpackage_models.ProductPackage, models.DO_NOTHING, db_column="id")
    pCPQuantity = models.IntegerField(db_column="PCPQuantity", blank=True, null=True)
    pCPCreateDate = models.DateTimeField(db_column="PackageCreateDate", blank=True, null=True)
    pCPPrice = models.DecimalField(db_column="PackagePrice", max_digits=18, decimal_places=2,  blank=True, null=True)


    class Meta:
        managed = True
        db_table ='tblProductContainedPackage'


class ServiceContainedPackage(models.Model):
    idSCP = models.AutoField( primary_key=True)
    product_packageId = models.ForeignKey(productpackage_models.ProductPackage, models.DO_NOTHING, db_column="id")
    medical_serviceId = models.ForeignKey(medical_models.Service, models.DO_NOTHING, db_column="ServiceID")
    sCPQuantity = models.IntegerField(db_column="PCPQuantity", blank=True, null=True)
    sCPCreateDate = models.DateTimeField(db_column="PackageCreateDate", blank=True, null=True)
    sCPPrice = models.DecimalField(db_column="PackagePrice", max_digits=18, decimal_places=2, blank=True, null=True)


    class Meta:
        managed = True
        db_table ='tblServiceContainedPackage'


