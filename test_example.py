from cal import shopping
import unittest
import pytest
import requests
"""from cal import calculate
import pytest


@pytest.mark.parametrize(
    "a,b,expected", [(2, 3, 6), (4, 5, 20), (0, 10, 0), (-1, 5, -5), (-2, -3, 6)])
def test_calculate(a, b, expected):
    assert calculate(a, b) == expected"""


""""
@pytest.fixture
def sample_data():
    return [1, 2, 3, 4, 5]


def test_sample_data(sample_data):
    assert len(sample_data) == 5
    assert sample_data[0] == 1
    assert sample_data[-1] == 5
    assert sum(sample_data) == 15
    assert all(isinstance(x, int) for x in sample_data)"""


"""import pytest


class Product:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity


class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product):
        self.items.append(product)

    def calculate_total_price(self, tax_rate=0.0, shipping_fee=0.0):
        subtotal = sum(item.price * item.quantity for item in self.items)
        tax = subtotal * tax_rate
        total = subtotal + tax + shipping_fee
        return total

    def apply_discount(self, discount_percentage):
        for item in self.items:
            item.price *= (1 - discount_percentage / 100)

    def checkout(self, payment_gateway):
        total_price = self.calculate_total_price()
        # In a real application, you'd interact with the payment_gateway here
        if payment_gateway.process_payment(total_price):
            # Place the order (logic not shown here)
            return True
        else:
            return False


class TestProductFunctions:
    def test_add_to_cart_successful(self):
        cart = Cart()
        product = Product("Widget", 10.0)
        cart.add_to_cart(product)
        assert len(cart.items) == 1
        assert cart.items[0] == product

    def test_calculate_total_price_accuracy(self):
        cart = Cart()
        cart.add_to_cart(Product("Widget A", 15.0))
        cart.add_to_cart(Product("Widget B", 20.0, 2))  # 2 of these
        total = cart.calculate_total_price(tax_rate=0.07, shipping_fee=5.0)
        expected_total = (15.0 + 20.0 * 2) * 1.07 + 5.0
        assert total == expected_total

    def test_apply_discount_correctly(self):
        cart = Cart()
        cart.add_to_cart(Product("Discounted Item", 50.0))
        cart.apply_discount(20)  # 20% discount
        assert cart.items[0].price == 40

    def test_checkout_successful_payment(self, mocker):
        # Mocking a payment gateway (would be a real integration in a production app)
        mock_payment_gateway = mocker.Mock()
        mock_payment_gateway.proces_payment.return_value = True

        cart = Cart()
        cart.add_to_cart(Product("Something", 100.0))
        result = cart.checkout(mock_payment_gateway)
        assert result is True"""


"""def cal_price(price, tax):
    return price + (price * tax)


class TestCalculatePrice(unittest.TestCase):
    def test_cal_price(self):
        self.assertEqual(cal_price(100, 0.2), 120)

    def test_cal_price_zero_tax(self):
        self.assertEqual(cal_price(200, 0), 200)


unittest.main()"""


"""def test_check_url():
    url = "https://scikit-learn.org/stable/"
    response = requests.get(url)
    assert response.status_code == 200


if __name__ == "__main__":
    pytest.main()"""


class TestShopping(unittest.TestCase):
    def test_shopping(self):
        price = 200
        discount = 20
        expected = 160
        discounted_price = shopping(price, discount)
        self.assertEqual(discounted_price, expected)


if __name__ == "__main__":
    unittest.main()
