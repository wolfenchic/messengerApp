from django.test import TestCase
from .views import profile
from django.core.urlresolvers import resolve


class profileTest(TestCase):
    def test_profile_page_resolves(self):
        profile_page=resolve('/accounts/profile/')
        self.assertEqual(profile_page.func, profile)


# Create your tests here.
