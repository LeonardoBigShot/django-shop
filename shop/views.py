from django import template
from django.shortcuts import get_object_or_404, render
from django.template import context, loader
from .models import Category, Product
from cart.forms import CartAddProductForm


def index(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.order_by('-created')
    context = {'products': products, 'categories': categories}
    return render(request, 'index.html', context)


def delivery(request):
    category = None
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'delivery.html', context)


def order(request):
    category = None
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'order.html', context)


def support(request):
    category = None
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'support.html', context)


def by_category(request, category_id):
    products = Product.objects.order_by('-created')
    categories = Category.objects.all()
    current_category = Category.objects.get(pk=category_id)
    context = {'products': products, 'categories': categories,
               'current_category': current_category}
    return render(request, 'shop/by_category.html', context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'card.html', {'product': product,
                                                        'cart_product_form': cart_product_form})
