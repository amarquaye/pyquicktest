"""
Python unit testing library by Jesse Amarquaye.
Simple project to mimic unittest; a builtin python testing framework.
"""

# Define a basic test case class
class TestCase:
    # Initialize the test case class
    def __init__(self):
        # Collect all methods in the class that start with 'test_'
        self._test_methods = [method for method in dir(self) if method.startswith('test_')]

    # Run all test methods and print results
    def run(self):
        # Initialize result counters
        results = {'total': 0, 'passed': 0, 'failed': 0}

        # Iterate over each test method
        for test_method in self._test_methods:
            # Increment total test count
            results['total'] += 1

            try:
                # Call the test method
                getattr(self, test_method)()
                # If the test method doesn't raise an AssertionError, mark it as passed
                results['passed'] += 1
                print(f"{test_method}: Passed")
            except AssertionError as e:
                # If an AssertionError is raised, mark the test as failed and print an error message
                results['failed'] += 1
                print(f"{test_method}: Failed - {e}")

        # Print overall test results
        print(f"\nResults: {results['passed']}/{results['total']} tests passed")

    # Custom assertion method for equality
    def assert_equal(self, actual, expected, message=None):
        # Raise AssertionError if actual is not equal to expected
        if actual != expected:
            # If no custom error message is provided, create a default one
            if message is None:
                message = f"Expected {expected}, but got {actual}"
            raise AssertionError(message)

    # Custom assertion method for truthiness
    def assert_true(self, expression, message=None):
        # Raise AssertionError if expression is not true
        if not expression:
            # If no custom error message is provided, create a default one
            if message is None:
                message = "Assertion failed: expression is not true"
            raise AssertionError(message)


# Example usage:

# # Define a test case class that inherits from SimpleTestCase
# class MyTests(SimpleTestCase):
#     # Define a test method for addition
#     def test_addition(self):
#         # Use the custom assert_equal method to check if 1 + 1 equals 2
#         self.assert_equal(1 + 1, 2)

#     # Define a test method for subtraction
#     def test_subtraction(self):
#         # Use the custom assert_equal method to check if 3 - 1 equals 2
#         self.assert_equal(3 - 1, 2)

#     # Define a test method that intentionally fails
#     def test_failure(self):
#         # Use the custom assert_equal method to check if 2 * 2 equals 5 (intentional failure)
#         self.assert_equal(2 * 2, 5)

# # Run the tests if the script is executed
# if __name__ == '__main__':
#     # Create an instance of the test case class
#     test_suite = MyTests()
#     # Run the tests
#     test_suite.run()
