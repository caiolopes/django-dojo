from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Product


@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    return render(request, 'detail.html', {'product': product})

