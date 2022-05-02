import unittest
from app.models import News

class NewsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.new_source = News("1234","The New York Times")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))