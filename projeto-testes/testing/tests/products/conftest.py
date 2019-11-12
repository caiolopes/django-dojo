import pytest
from mixer.backend.django import mixer


@pytest.fixture
def quantity():
    return 0


@pytest.fixture
def product(quantity, db):
    return mixer.blend('products.Product', quantity=quantity)