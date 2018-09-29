from django.test import TestCase, Client
from django.urls import reverse

from rest_framework.test import APIClient

from fixtures.utils import get_fixtures

from apps.news.models import News, Topics

class NewsAPI(TestCase):

    fixtures = get_fixtures()

    def test_list_news(self):
        client = APIClient()
        news = News.objects.all()
        response = client.get(reverse('news:api:list'))
        self.assertEqual(200, response.status_code)
        self.assertEqual(news.count(), len(response.data))

        news = News.objects.filter(status='draft')
        response = client.get(reverse('news:api:list') + '?status=draft')
        self.assertEqual(200, response.status_code)
        self.assertTrue(news.count() > 0)
        self.assertEqual(news.count(), len(response.data))
        
        news = News.objects.filter(status='publish')
        response = client.get(reverse('news:api:list') + '?status=publish')
        self.assertEqual(200, response.status_code)
        self.assertTrue(news.count() > 0)
        self.assertEqual(news.count(), len(response.data))

        news = News.objects.filter(status='deleted')
        response = client.get(reverse('news:api:list') + '?status=deleted')
        self.assertEqual(200, response.status_code)
        self.assertTrue(news.count() > 0)
        self.assertEqual(news.count(), len(response.data))

        topics_id = Topics.objects.first().id
        news = News.objects.filter(topics__pk=topics_id)
        response = client.get(reverse('news:api:list') + '?topics=' + str(topics_id))
        self.assertEqual(200, response.status_code)
        self.assertTrue(news.count() > 0)
        self.assertEqual(news.count(), len(response.data))

    def test_create_news(self):
        client = APIClient()
        topics_id = Topics.objects.first().id
        data = {
            'title': 'test',
            'status': 'draft',
            'topics': [topics_id]
        }
        response = client.post(reverse('news:api:list'), data, format='json')
        self.assertEqual(201, response.status_code)
        news = News.objects.last()
        self.assertEqual(news.id, response.data['id'])
        self.assertEqual(news.title, 'test')
        
    def test_update_news(self):
        client = APIClient()
        news = News.objects.filter(status='draft').first()
        news_id = news.id
        topics_id = Topics.objects.exclude(
            pk__in=news.topics.all()).values_list('id', flat=True)
        new_title = 'copy of ' + news.title

        data = {
            'title': new_title,
            'status': 'publish',
            'topics': topics_id
        }
        response = client.put(reverse('news:api:detail', args=[news.id]), data, format='json')
        self.assertEqual(200, response.status_code)
        news = News.objects.filter(status='publish', title=new_title)
        self.assertTrue(news.exists())
        self.assertEqual(news_id, response.data['id'])
        for index, topic_id in enumerate(topics_id):
            self.assertEqual(topic_id, response.data['topics'][index])
        
    def test_delete_news(self):
        client = APIClient()
        news = News.objects.first()
        news_id = news.id
        response = client.delete(reverse('news:api:detail', args=[news.id]))
        self.assertEqual(204, response.status_code)
        self.assertFalse(News.objects.filter(pk=news_id).exists())

    def test_delete_status_news(self):
        client = APIClient()
        news = News.objects.exclude(status='deleted').first()
        self.assertFalse(news.status == 'deleted')
        news_id = news.id
        response = client.delete(reverse('news:api:delete_status', args=[news.id]))
        self.assertEqual(204, response.status_code)
        news = News.objects.get(pk=news_id)
        self.assertTrue(news.status == 'deleted')
    
    def test_delete_data_news(self):
        client = APIClient()
        news = News.objects.first()
        news_id = news.id
        response = client.delete(reverse('news:api:delete_data', args=[news.id]))
        self.assertEqual(204, response.status_code)
        self.assertFalse(News.objects.filter(pk=news_id).exists())
