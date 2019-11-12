from django.test import TestCase
from django.urls import reverse, resolve

from products.views import product_detail


def test_detail_url(product):
    path = reverse('detail', kwargs=dict(pk=product.pk))
    assert resolve(path).func == product_detail