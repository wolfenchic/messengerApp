from django.test import TestCase
from .views import get_home_page
from django.core.urlresolvers import resolve


class HomePageTest(TestCase):
    def test_home_page_resolves(self):
        home_page=resolve('/')
        self.assertEqual(home_page.func, get_home_page)

