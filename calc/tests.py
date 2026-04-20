from django.test import TestCase
from django.urls import reverse


class CalcViewTests(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello Baba')

    def test_add_view_returns_sum(self):
        response = self.client.get(reverse('add'), {'num1': 7, 'num2': 5})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Result: 12')

    def test_add_view_handles_invalid_input(self):
        response = self.client.get(reverse('add'), {'num1': 'abc', 'num2': 5})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Please enter valid whole numbers.')
