Sure, here are examples of two unit tests, two mock tests, and two integration tests for an e-commerce project using FastAPI, React, and MongoDB:

### Unit Tests

#### 1. Unit Test for Product Model

This test ensures the correct behavior of the product model in isolation.

```python
# test_models.py
import unittest
from models import Product

class TestProductModel(unittest.TestCase):

    def test_create_product(self):
        product = Product(name="Test Product", price=29.99, description="A test product")
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.price, 29.99)
        self.assertEqual(product.description, "A test product")

if __name__ == '__main__':
    unittest.main()
```

#### 2. Unit Test for Order Calculation

This test verifies the calculation logic for orders.

```python
# test_order.py
import unittest
from models import Order, Product

class TestOrder(unittest.TestCase):

    def test_order_total(self):
        product1 = Product(name="Test Product 1", price=10.00)
        product2 = Product(name="Test Product 2", price=20.00)
        order = Order(products=[product1, product2])
        self.assertEqual(order.total, 30.00)

if __name__ == '__main__':
    unittest.main()
```

### Mock Tests

#### 1. Mock Test for Sending Confirmation Email

This test uses a mock object to simulate sending a confirmation email.

```python
# test_email_service.py
import unittest
from unittest.mock import Mock, patch
from services import send_confirmation_email

class TestEmailService(unittest.TestCase):

    @patch('services.smtplib.SMTP')
    def test_send_confirmation_email(self, MockSMTP):
        mock_smtp_instance = MockSMTP.return_value
        send_confirmation_email('customer@example.com', 'Order Confirmed')
        mock_smtp_instance.sendmail.assert_called_with('no-reply@example.com', 'customer@example.com', 'Order Confirmed')

if __name__ == '__main__':
    unittest.main()
```

#### 2. Mock Test for Payment Processing

This test mocks the payment gateway to verify the payment processing functionality.

```python
# test_payment_service.py
import unittest
from unittest.mock import Mock, patch
from services import process_payment

class TestPaymentService(unittest.TestCase):

    @patch('services.payment_gateway')
    def test_process_payment(self, mock_payment_gateway):
        mock_payment_gateway.charge.return_value = {"status": "success", "transaction_id": "12345"}
        response = process_payment('card_abc', 50.00)
        self.assertEqual(response['status'], 'success')
        self.assertEqual(response['transaction_id'], '12345')

if __name__ == '__main__':
    unittest.main()
```

### Integration Tests

#### 1. Integration Test for Creating a Product

This test verifies the endpoint for creating a product in FastAPI.

```python
# test_api.py
import unittest
from fastapi.testclient import TestClient
from main import app

class TestProductAPI(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_create_product(self):
        response = self.client.post("/products/", json={"name": "Test Product", "price": 29.99, "description": "A test product"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["name"], "Test Product")
        self.assertEqual(response.json()["price"], 29.99)

if __name__ == '__main__':
    unittest.main()
```

#### 2. Integration Test for User Registration

This test checks the user registration functionality.

```python
# test_user_registration.py
import unittest
from fastapi.testclient import TestClient
from main import app

class TestUserRegistrationAPI(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_user_registration(self):
        response = self.client.post("/register/", json={"username": "testuser", "email": "test@example.com", "password": "password"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["username"], "testuser")
        self.assertEqual(response.json()["email"], "test@example.com")

if __name__ == '__main__':
    unittest.main()
```

These examples cover different aspects of an e-commerce project, including unit tests for individual components, mock tests for services interacting with external systems, and integration tests for API endpoints.
