import pytest


@pytest.mark.parametrize('quantity,expected', [(1, True), (0, False)],
                         ids=["Qtd:1,HasStock:True", "Qtd:0,HasStock:False"])
def test_has_stock(product, expected, db):
    # when
    has_stock = product.has_stock

    # then
    assert expected == has_stock
