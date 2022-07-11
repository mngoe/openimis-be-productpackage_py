import graphene
from core import ExtendedConnection
from core.schema import OrderedDjangoFilterConnectionField, DjangoObjectType

from productpackage.models import ProductPackage, ProductContainedPackage, ServiceContainedPackage


class ProductPackageGQLType(DjangoObjectType):



    class Meta:
        model = ProductPackage
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            "PackageType": ["exact"],
            "PackageName": ["exact", "icontains"],
            "PackageDate": ["exact", "lt", "lte", "gt", "gte"],
        }
        connection_class = ExtendedConnection

class ProductContainedPackageGQLType(DjangoObjectType):



    class Meta:
        model = ProductContainedPackage
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            "productpackageId": ["exact"],
            "PCPDate": ["exact", "lt", "lte", "gt", "gte"],
        }
        connection_class = ExtendedConnection

class ServiceContainedPackageGQLType(DjangoObjectType):



    class Meta:
        model = ServiceContainedPackage
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            "product_packageId": ["exact"],
            "medical_serviceId": ["exact"],
            "SCPDate": ["exact", "lt", "lte", "gt", "gte"],
        }
        connection_class = ExtendedConnection



class Query(graphene.ObjectType):
    ProductPackage = OrderedDjangoFilterConnectionField(
        ProductPackageGQLType,
        getProductPackId=graphene.Int(),
        get_byName=graphene.String(),
        orderBy=graphene.List(of_type=graphene.String),
        items=graphene.List(of_type=graphene.String),
        services=graphene.List(of_type=graphene.String),
    )

    ProductContainedPackage = OrderedDjangoFilterConnectionField(
        ProductContainedPackageGQLType,
        productPack_foreignKey=graphene.Int(),
        code_is_not=graphene.String(),
        orderBy=graphene.List(of_type=graphene.String),
        items=graphene.List(of_type=graphene.String),
    )

    ServiceContainedPackage = OrderedDjangoFilterConnectionField(
        ServiceContainedPackageGQLType,
        productPack_foreignKey_service=graphene.Int(),
        get_byName=graphene.String(),
        orderBy=graphene.List(of_type=graphene.String),
        items=graphene.List(of_type=graphene.String),
        services=graphene.List(of_type=graphene.String),
    )