from django.conf import settings
from django.db.models import query
from django.http import request
from rest_framework import generics, serializers, status
from rest_framework.response import Response
from rest_framework import viewsets, status



from .models import Factura
from .serializers import FacturaSerializer


class ReceiptViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Factura.objects.all()
        serializer = FacturaSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = FacturaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        product = Factura.objects.get(id=pk)
        serializer = FacturaSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        product = Factura.objects.get(id=pk)
        serializer = FacturaSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        product = Factura.objects.get(id=pk)   
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


