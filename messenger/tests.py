from django.test import TestCase
from .views import inbox, message
from django.core.urlresolvers import resolve

# Create your tests here.
class InboxTest(TestCase):
    def test_inbox_page_resolves(self):
        inbox_page=resolve('/messenger/inbox/')
        self.assertEqual(inbox_page.func, inbox)

class MessageTest(TestCase):
     def test_message_page_resolves(self):
        message_page=resolve('/messenger/mail/1/')
        self.assertEqual(message_page.func, message)

class test_message_requires_id(TestCase):
    def test_message_requires_id(self):
        response = self.client.get('messenger/mail/')
        self.assertEqual(response.status_code, 404)