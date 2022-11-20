from django.test import TestCase
from dashboard.models import TodoDb


class TodoDbModelTest(TestCase):
    def setUp(self):
        self.test_task = TodoDb.objects.create(
            author='test name',
            header='test header',
            content='test content',
            slave='test slave',
        )

    def test_data_in_bd(self):
        task = TodoDb.objects.get(author="test name")
        self.assertEqual(task.content, 'test content')
