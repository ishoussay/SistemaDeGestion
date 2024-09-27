from django.urls import path
from .views import crear_orden_compra

urlpatterns = [
    path('crear-orden-compra/', crear_orden_compra, name='crear_orden_compra'),
]
