
from django.test import SimpleTestCase


class DjangoSimpleTestCase(SimpleTestCase):

    def setUp(self):
        pass

    def test_easy(self):
        self.assertTrue(True)

    def test_easy_2(self):
        self.assertTrue(True)
