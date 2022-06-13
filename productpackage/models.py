""" Importing model from django.db with
    product and medical module """
from django.db import models
# from django.db.models import Count

# Create your models here.
from product import models as product_models
from medical import models as medical_models
from product.models import Product


class ProductPackage(models.Model):
    """ class representing the package """

    ID = models.AutoField(db_column="PackageID", primary_key=True)
    PackageType = models.CharField(db_column="PackageType", max_length=20, blank=True, null=True)
    PackageName = models.CharField(db_column="PackageName", max_length=100, blank=True, null=True)
    PackageDate = models.DateTimeField(db_column="PackageDate",
                                       blank=True, null=True)
    PackagePrice = models.DecimalField(db_column="PackagePrice",
                                       max_digits=18, decimal_places=2, blank=True, null=True)
    PackageCheckBox = models.BooleanField(default=True)

    @classmethod
    def delete_productpackagerow(cls, id_productpackagerow):
        """ delete a row in productPackage table """

        cls.objects.find(idSCP=id_productpackagerow).delete()

    class Meta:
        managed = True
        db_table = 'tblProducPackage'


class ProductContainedPackage(models.Model):
    """class representing relation between package and product """

    idPCP = models.AutoField(primary_key=True)
    productId = models.ForeignKey(product_models.Product,
                                  models.DO_NOTHING, db_column="ProductId")
    productpackageId = models.ForeignKey(ProductPackage,
                                         models.DO_NOTHING, db_column="id")
    PCPQuantity = models.IntegerField(db_column="PCPQuantity",
                                      blank=True, null=True)
    PCPDate = models.DateTimeField(db_column="PackageDate",
                                   blank=True, null=True)
    PCPPrice = models.DecimalField(db_column="PackagePrice",
                                   max_digits=18, decimal_places=2, blank=True, null=True)

    @classmethod
    def sum_quantityproduct(cls):
        """ set the sum of quantity of product"""
        return cls.objects.all().aggregate(sum('PCPQuantity'))

    @classmethod
    def delete_productcontainedpackagerow(cls, id_productrow):
        """ delete a row in ProductContainedPackage table """
        cls.objects.find(idPCP=id_productrow).delete()

    class Meta:
        managed = True
        db_table = 'tblProductContainedPackage'


class ServiceContainedPackage(models.Model):
    """class representing relation between package and services """

    idSCP = models.AutoField(primary_key=True)
    product_packageId = models.ForeignKey(ProductPackage,
                                          models.DO_NOTHING, db_column="id")
    medical_serviceId = models.ForeignKey(medical_models.Service,
                                          models.DO_NOTHING, db_column="ServiceID")
    SCPQuantity = models.IntegerField(db_column="PCPQuantity",
                                      blank=True, null=True)
    SCPDate = models.DateTimeField(db_column="PackageDate",
                                   blank=True, null=True)
    SCPPrice = models.DecimalField(db_column="PackagePrice",
                                   max_digits=18, decimal_places=2, blank=True, null=True)

    @classmethod
    def sum_quantityservice(cls):
        """ this fucntion returns the sum of the values of the entries of SCPQuantity field """
        return cls.objects.all().aggregate(sum('SCPQuantity'))

    @classmethod
    def delete_servicecontainedpackrow(cls, id_servicerow):
        """ delete a row in ServiceContainedPackage table """
        try:
            cls.objects.find(idSCP=id_servicerow).delete()
        except cls.DoesNotExist:
            print('Service  with id "%f" does not exist.' % id_servicerow)

    class Meta:
        managed = True
        db_table = 'tblServiceContainedPackage'


def sum_quantity_productservice():
    """ fucntion that counts the number of entries from the table product and table services """
    return sum(Product.objects.filter(db_column="ProdID").count(),
               medical_models.Service.
               objects.filter(db_column="ServiceID").count())


def delete_productrow(id_productrow):
    """ delete a row in product table """
    try:
        Product.objects.find(id=id_productrow).delete()
    except Product.DoesNotExist:
        print('Product  with id "%f" does not exist.' % id_productrow)
