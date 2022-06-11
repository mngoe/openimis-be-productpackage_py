from django.db import models
from django.db.models import Count
from product import models as product_models
#from sql_util.tests.models import Product
from product.models import Product

from productpackage import models as productpackage_models
from medical import models as medical_models

# Create your models here.
class ProductPackage(models.Model):
    id = models.AutoField( primary_key=True)
    packageType = models.CharField(max_length=20, blank=True, null=True)
    packageName = models.CharField(max_length=100, blank=True, null=True)
    packageCreateDate = models.DateTimeField()
    packagePrice = models.DecimalField(max_digits=18, decimal_places=2,  blank=True, null=True)
    PackageCheckBox = models.BooleanField(default= True)

    @classmethod
    def delete_productpackagerow(cls, id_productpackagerow):  # delete a row in productPackage table
        cls.objects.find(idSCP=id_productpackagerow).delete()


    class Meta:
        managed = True
        db_table ='tblProductPackage'

    ### CRUD for Productpackage model

    # Define a function to create an entry
    #@classmethod
    #def createproductpackage(cls):




class ProductContainedPackage(models.Model):
    idPCP = models.AutoField( primary_key=True)
    productId = models.ForeignKey(product_models.Product, models.DO_NOTHING, db_column="ProductId")
    productpackageId = models.ForeignKey(productpackage_models.ProductPackage, models.DO_NOTHING, db_column="id")
    pCPQuantity = models.IntegerField( blank=True, null=True)
    pCPCreateDate = models.DateTimeField(blank=True, null=True)
    pCPPrice = models.DecimalField(max_digits=18, decimal_places=2,  blank=True, null=True)


    @classmethod
    def sum_quantityproduct(cls):
        return cls.objects.all().aggregate(sum('pCPQuantity'))

    @classmethod
    def delete_productcontainedpackagerow(cls, id_productrow ): #delete a row in ProductContainedPackage table
        cls.objects.find(idPCP = id_productrow).delete()


    class Meta:
        managed = True
        db_table ='tblProductContainedPackage'



class ServiceContainedPackage(models.Model):
    idSCP = models.AutoField( primary_key=True)
    product_packageId = models.ForeignKey(productpackage_models.ProductPackage, models.DO_NOTHING, db_column="id")
    medical_serviceId = models.ForeignKey(medical_models.Service, models.DO_NOTHING, db_column="ServiceID")
    sCPQuantity = models.IntegerField()
    sCPCreateDate = models.DateTimeField()
    sCPPrice = models.DecimalField(max_digits=18, decimal_places=2)

    @classmethod
    def sum_quantityservice(cls):  # this fucntion returns the sum of the values of the entries of SCPQuantity field
        return cls.objects.all().aggregate(sum('sCPQuantity'))

    @classmethod
    def delete_servicecontainedpackagerow(cls, id_servicerow):  # delete a row in ServiceContainedPackage table
        try:
            cls.objects.find(idSCP=id_servicerow).delete()
        except cls.DoesNotExist:
            print('Service  with id "%s" does not exist.' % id_servicerow)

    class Meta:
        managed = True
        db_table ='tblServiceContainedPackage'





def sum_quantity_productservice(): # fucntion that counts the number of entries from the table product and table services
    return sum(Product.objects.filter(db_column="ProdID").count(),
               medical_models.Service.objects.filter(db_column ="ServiceID").count())

def delete_productrow(self, id_productrow):  # delete a row in product table
    try:
        Product.objects.find(id = id_productrow).delete()
    except Product.DoesNotExist:
        print('Product  with id "%s" does not exist.' % id_productrow)


