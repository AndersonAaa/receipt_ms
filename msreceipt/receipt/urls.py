from django.urls import path

from .views import ReceiptViewSet

urlpatterns = [
    path('receipt', ReceiptViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('receipt/<str:pk>', ReceiptViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]