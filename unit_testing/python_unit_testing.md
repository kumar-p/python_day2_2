# Different component of unit testing

- **Test Case:** An individual unit of testing. It examines the output for a given input set.
- **Test Suit:** A collection of test cases, test suites, or both. They’re grouped and executed as a whole.
- **Test fixture:** A group of actions required to set up an environment for testing. It also includes the teardown processes after the tests run.
- **Test runner:** A component that handles the execution of tests and communicates the results to the user.

## UnitTest Class

The `unittest` module in Python provides a framework for creating and running tests. The `UnitTest` class is used to create individual test cases by subclassing it and defining test methods.

### Example

```python
import unittest

class TestMathOperations(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)

if __name__ == '__main__':
    unittest.main()
```
Once we have writtent some unit tests we have two ways to run them.
1. Make the test module executable
2. Use the command line interface of unit tests

to make the test module executable we we add the following code at the end of module
```Python
if __name__ == '__main__':
    unittest.main()
```

In above example:
- `TestMathOperations` is a subclass of `unittest.TestCase`.
- `test_addition` and `test_subtraction` are individual test methods.
- `unittest.main()` is used to run the tests when the script is executed.

## Naming Conventions for Test Discovery

To ensure that your tests are automatically discovered and run by the test runner, it is important to follow certain naming conventions:

1. **Test Module Names:** Test modules (files) should start with `test_` or end with `_test`. For example, `test_math_operations.py` or `math_operations_test.py`.
2. **Test Class Names:** Test classes should start with `Test`. For example, `TestMathOperations`.
3. **Test Method Names:** Test methods should start with `test_`. For example, `test_addition`.

By following these conventions, you can leverage test discovery features provided by test runners like `unittest`, `pytest`, and others.

## Grouping Your Tests With the TestSuite Class

The `TestSuite` class in the `unittest` module allows you to aggregate tests that should be executed together. This can be useful when you want to group certain tests and run them as a batch.

### Example

```python
import unittest

class TestMathOperations(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)

class TestStringOperations(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestMathOperations('test_addition'))
    suite.addTest(TestMathOperations('test_subtraction'))
    suite.addTest(TestStringOperations('test_upper'))
    suite.addTest(TestStringOperations('test_isupper'))

    runner = unittest.TextTestRunner()
    runner.run(suite)
```

In this example:
- `TestMathOperations` and `TestStringOperations` are subclasses of `unittest.TestCase`.
- Individual test methods are added to a `TestSuite` instance.
- `unittest.TextTestRunner` is used to run the suite of tests.

By using `TestSuite`, you can control the order of test execution and group related tests together.

## Using Mocking in Unit Tests

Mocking is a technique used in unit testing to replace real objects with mock objects to simulate the behavior of complex, real objects. This is particularly useful when testing components that interact with external systems such as databases, APIs, or other services.

Here is an example of how to use the `unittest.mock` module to mock an external API call:

```python
import unittest
from unittest.mock import patch
import requests

def get_weather(city):
    response = requests.get(f'http://api.weather.com/{city}')
    return response.json()

class TestWeatherAPI(unittest.TestCase):
    @patch('requests.get')
    def test_get_weather(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.json.return_value = {'weather': 'sunny'}

        result = get_weather('London')
        self.assertEqual(result['weather'], 'sunny')
        mock_get.assert_called_once_with('http://api.weather.com/London')

if __name__ == '__main__':
    unittest.main()
```

In this example:
- The `@patch` decorator is used to replace the `requests.get` method with a mock object.
- The `mock_get.return_value` is set to a mock response object.
- The `mock_response.json.return_value` is set to return a predefined JSON response.
- The test verifies that the `get_weather` function returns the expected result and that the `requests.get` method was called with the correct URL.

Mocking allows you to isolate the unit of work being tested and ensure that your tests are not dependent on external systems, making them more reliable and faster to run.