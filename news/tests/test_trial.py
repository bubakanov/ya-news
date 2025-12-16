from unittest import skip

from django.test import TestCase

from news.models import News


@skip
class TestNews(TestCase):
    TITLE = "News"
    TEXT = "News"

    @classmethod
    def setUpTestData(cls):
        cls.news = News.objects.create(
            title=cls.TITLE,
            text=cls.TEXT
        )

    def test_successful_creation(self):
        news_count = News.objects.count()
        self.assertEqual(news_count, 1)

    def test_title_exists(self):
        self.assertEqual(self.TITLE, self.news.title)
