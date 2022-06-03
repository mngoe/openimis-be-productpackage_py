import uuid
from django.db import models
from product import models as product_models

# Create your models here.
class ProductPackage(product_models.Product):
    package = models.CharField(db_column="ProductPackage", max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "tblProduct"
