from django.test import TestCase
from .views import profile
from django.core.urlresolvers import resolve


class profileTest(TestCase):
    def test_profile_page_resolves(self):
        profile_page=resolve('/accounts/profile/')
        self.assertEqual(profile_page.func, profile)

class TestAccounts(TestCase):
    def test_anonymous_user_can_not_view_profile(self):
        response = self.client.get('/accounts/profile/')
        self.assertEqual(response.status_code, 302)

# Create your tests here.
