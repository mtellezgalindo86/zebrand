from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import Product
from .serializers import ProductSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    """
       Vista para listar y crear productos.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
       Vista para obtener, actualizar y eliminar un producto específico.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]

    def get_permissions(self):
        """
              Obtiene los permisos de la vista.
              Los usuarios no autenticados pueden acceder a las solicitudes GET.
              Se verifica el encabezado de autorización para las otras solicitudes.
        """
        if self.request.method == 'GET':
            return [AllowAny()]

        try:
            authorization_header = self.request.headers['Authorization']
            if not authorization_header.startswith('Token'):
                raise AuthenticationFailed('Invalid token')
        except KeyError:
            raise AuthenticationFailed('No token provided')

        return super().get_permissions()