from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from users.models import User
from products.models import Product, ProductCategory, Basket


def index(request):
    return render(request, 'products/index.html',)

def products(request):
    products = Product.objects.all()
    categories = ProductCategory.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'products/products.html', context)

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, qnt=1)
    else:
        basket = baskets.first()
        basket.qnt += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


