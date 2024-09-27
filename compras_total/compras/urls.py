from django.urls import path
from . import views

urlpatterns = [
    path('crear-orden-compra/', views.crear_orden_compra, name='crear_orden_compra'),
    path('negociar/<int:proveedor_id>/', views.negociar_con_proveedor, name='negociar_con_proveedor'),
    path('historial_negociaciones/<int:proveedor_id>/', views.historial_negociaciones, name='historial_negociaciones'),
]
