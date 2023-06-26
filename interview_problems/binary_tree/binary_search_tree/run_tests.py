import unittest

if __name__ == '__main__':
    # Discover and load tests from the 'tests' folder
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests')

    # Create a test runner and run the tests
    test_runner = unittest.TextTestRunner()
    test_runner.run(test_suite)
