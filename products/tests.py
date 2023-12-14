# from http import HTTPStatus
# from django.test import TestCase
#
# from django.urls import reverse
#
# from products.models import Product, ProductCategory
#
#
# class IndexViewTestCase(TestCase):
#     def test_view(self):
#         path = reverse('index')
#         response = self.client.get(path)
#         self.assertEqual(response.status_code, HTTPStatus.OK)
#         self.assertTemplateUsed(response, 'products/index.html')
#
#
# class ProductsListViewTestCase(TestCase):
#     fixtures = ['categories.json', 'good.json']
#
#     def setUp(self):
#         self.products = Product.objects.all()
#
#     def test_list_products(self):
#         path = reverse('products')
#         response = self.client.get(path)
#
#         self.assertEqual(response.status_code, HTTPStatus.OK)
#         self.assertTemplateUsed(response, 'products/products.html')
#         self.assertEqual(list(response.context_data['object_list']), list(self.products[:3]))
#
#     def test_list_categories(self):
#         category = ProductCategory.objects.first()
#         path = reverse('category',  kwargs={'category_id': category.id})
#         response = self.client.get(path)
#
#         self.assertEqual(response.status_code, HTTPStatus.OK)
#         self.assertTemplateUsed(response, 'products/products.html')
#         self.assertEqual(
#             list(response.context_data['object_list']),
#             list(self.products.filter(category_id=category.id)))
#
#
