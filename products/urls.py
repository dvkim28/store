from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from products.views import basket_add, basket_remove, indexView, ProductsListView

urlpatterns = [
    path('', indexView.as_view(), name='index'),
    path('products', ProductsListView.as_view(), name='products'),
    path('category/<int:category_id>/', ProductsListView.as_view(), name='category'),
    path('page/<int:page>/',  ProductsListView.as_view(), name='paginator'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
