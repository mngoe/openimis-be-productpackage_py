import uuid
from django.db import models
from product import models as product_models

# Create your models here.
class ProductPackage(models.Model):
    productType = models.CharField(db_column="productType", max_length=100, blank=True, null=True)
    productId = models.ForeignKey(
        product_models.Product, models.DO_NOTHING, db_column="ProductId"
    )
