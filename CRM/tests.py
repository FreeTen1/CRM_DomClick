from django.test import TestCase

from .models import Client, Worker, Query


class CemTestCases(TestCase):
    def setUp(self) -> None:
        self.client = Client.objects.create(name='Андрей', last_name='Прист', email='kjk@gmail.com')
        self.worker = Worker.objects.create(name='Юлий', last_name='Гай', email='cezar@gmail.com', position='Простой рабочий')
        self.query = Query.objects.create(client=self.client, type='RE', status='OP')
