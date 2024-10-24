As a Python full stack developer, you will likely need to write several types of tests to ensure your code is robust, reliable, and free of defects. Here are the main types of tests you might write, along with examples for each:

### 1. Unit Tests

Unit tests focus on testing individual components or functions in isolation.

Example:

```python
# test_calculator.py
import unittest
from calculator import add, subtract

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, -1), 0)

if __name__ == '__main__':
    unittest.main()
```

### 2. Integration Tests

Integration tests ensure that multiple components or systems work together as expected.

Example:

```python
# test_api.py
import unittest
import requests

class TestAPI(unittest.TestCase):

    def test_get_user(self):
        response = requests.get('http://example.com/api/user/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('username', response.json())

if __name__ == '__main__':
    unittest.main()
```

### 3. Functional Tests

Functional tests verify that the system functions correctly from the end-user's perspective.

Example:

```python
# test_login.py
import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        self.driver.get('http://example.com/login')
        self.driver.find_element_by_name('username').send_keys('testuser')
        self.driver.find_element_by_name('password').send_keys('password')
        self.driver.find_element_by_name('submit').click()
        self.assertIn('Welcome', self.driver.page_source)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
```

### 4. End-to-End (E2E) Tests

E2E tests cover complete workflows to ensure the entire application works as intended.

Example:

```python
# test_end_to_end.py
import unittest
from selenium import webdriver

class TestEndToEnd(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_end_to_end(self):
        self.driver.get('http://example.com')
        self.driver.find_element_by_link_text('Sign Up').click()
        self.driver.find_element_by_name('username').send_keys('newuser')
        self.driver.find_element_by_name('password').send_keys('newpassword')
        self.driver.find_element_by_name('submit').click()
        self.assertIn('Welcome newuser', self.driver.page_source)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
```

### 5. Performance Tests

Performance tests assess the speed, responsiveness, and stability of the application under various conditions.

Example:

```python
# test_performance.py
import unittest
import time
from myapp import load_data

class TestPerformance(unittest.TestCase):

    def test_load_data_performance(self):
        start_time = time.time()
        load_data()
        duration = time.time() - start_time
        self.assertLess(duration, 2)  # Expect the load_data function to run in less than 2 seconds

if __name__ == '__main__':
    unittest.main()
```

### 6. Security Tests

Security tests focus on identifying vulnerabilities in the application.

Example:

```python
# test_security.py
import unittest
import requests

class TestSecurity(unittest.TestCase):

    def test_sql_injection(self):
        payload = {"username": "admin'--", "password": "password"}
        response = requests.post('http://example.com/login', data=payload)
        self.assertNotIn('admin', response.text)  # The application should not be vulnerable to SQL injection

if __name__ == '__main__':
    unittest.main()
```

### 7. Mock Tests

Mock tests use mock objects to simulate the behavior of real objects to test the interaction between different components.

Example:

```python
# test_email_service.py
import unittest
from unittest.mock import Mock, patch
from email_service import send_email

class TestEmailService(unittest.TestCase):

    @patch('email_service.smtplib.SMTP')
    def test_send_email(self, MockSMTP):
        mock_smtp_instance = MockSMTP.return_value
        send_email('test@example.com', 'Subject', 'Body')
        mock_smtp_instance.sendmail.assert_called_with('from@example.com', 'test@example.com', 'Subject\n\nBody')

if __name__ == '__main__':
    unittest.main()
```

These examples provide a foundation for writing various types of tests in Python. Each type of test has its own importance and helps ensure the reliability and quality of your software.
