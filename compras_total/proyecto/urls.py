from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('compras/', include('compras.urls')),  # Incluir las URLs de la app "compras"
]
