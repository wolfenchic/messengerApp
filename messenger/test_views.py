from django.test import TestCase
from .views import *
from django.contrib.auth.models import User

class MessageViewsTest(TestCase):
     def test_inbox_template(self):
        response = self.client.get('/messenger/inbox/')
        self.assertTemplateUsed(response, "messenger/inbox.html")
        
class Message_does_not_exist(TestCase):
    def test_mail_template(self):
        response = self.client.get('messenger/message/1')
        self.assertEqual(response.status_code, 404)

    def test_view_message_that_exists(self):
        sender = User(username="sender")
        sender.save()

        recipient = User(username="receiver")
        recipient.save()

        message = Message(
            subject = "Test Subject",
            body = "Test Body",
            sender = sender,
            recipient = recipient)
        message.save()

        response = self.client.get('/messenger/message/1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "messenger/mail.html")