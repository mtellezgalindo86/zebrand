from django.contrib import admin
from django.urls import path,include
from catalog.views import ProductListCreateView
from catalog.views import ProductRetrieveUpdateDestroyView
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from . import views
#
#
# Configuración de la vista de esquema Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="API Productos",
        default_version='v1',
        description="Esta es una documentacion del servicio para Zebrans",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="martin.tellez.g86@icloud.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Rutas de la aplicación
    path('admin/', admin.site.urls),
    path('products/', ProductListCreateView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-detail'),
    # Rutas de autenticación proporcionadas por Django REST Framework
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/profile/', views.profile_view, name='profile'),

    # Rutas para la documentación de API con Swagger y ReDoc
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
