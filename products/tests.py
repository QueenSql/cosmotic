from django.test import TestCase

# Create your tests here.

class BasicTestCase(TestCase):
    """
    A basic placeholder test case.
    """
    def test_example(self):
        """
        Dummy test to check the test runner.
        """
        self.assertEqual(1 + 1, 2)
