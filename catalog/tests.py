from django.test import RequestFactory
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from catalog.models import User
from catalog.views import ProductListCreateView, ProductRetrieveUpdateDestroyView
from catalog.models import Product


class ProductListCreateViewTestCase(APITestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)

    def test_create_product(self):
        url = '/products/'
        data = {
            'sku': 'ABC123',
            'name': 'Test Product',
            'price': '9.99',
            'brand': 'Test Brand'
        }

        request = self.factory.post(url, data, format='json', content_type='application/json')
        request.META['HTTP_AUTHORIZATION'] = f'Token {self.token.key}'

        view = ProductListCreateView.as_view()
        response = view(request)

        self.assertEqual(response.status_code, 201)


class ProductRetrieveUpdateDestroyViewTestCase(APITestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.product = Product.objects.create(sku='ABC123', name='Test Product', price='9.99', brand='Test Brand')

    def test_update_product(self):
        url = f'/products/{self.product.pk}/'
        data = {
            'sku': 'DEF456',
            'name': 'Updated Product',
            'price': '19.99',
            'brand': 'Updated Brand'
        }

        request = self.factory.put(url, data, format='json', content_type='application/json')
        request.META['HTTP_AUTHORIZATION'] = f'Token {self.token.key}'

        view = ProductRetrieveUpdateDestroyView.as_view()
        response = view(request, pk=self.product.pk)

        self.assertEqual(response.status_code, 200)

    def test_delete_product(self):
        url = f'/products/{self.product.pk}/'

        request = self.factory.delete(url)
        request.META['HTTP_AUTHORIZATION'] = f'Token {self.token.key}'

        view = ProductRetrieveUpdateDestroyView.as_view()
        response = view(request, pk=self.product.pk)

        self.assertEqual(response.status_code, 204)
