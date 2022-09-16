from django.test import SimpleTestCase

from . import views

# Create your tests here.


class TestCases(SimpleTestCase):
    def test_remove_duplicate(self):
        input = [1, 2, 2, 2, 3, 4, 5, 7, 7, 7, 7]
        required_res = [1, 2, 3, 4, 5, 7]

        actual_res = views.remove_duplicate(input)

        self.assertEqual(required_res, actual_res)
