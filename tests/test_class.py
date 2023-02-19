from Shop.shop_main import Product


def test_class():
    test = Product("Apple", 10000, 3)
    assert test.get_price() == 30000
    assert test.get_discount_price() == 2000.0
