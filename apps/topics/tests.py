from django.test import TestCase, Client
from django.urls import reverse

from rest_framework.test import APIClient

from fixtures.utils import get_fixtures

from apps.topics.models import Topics

class TopicsAPI(TestCase):

    fixtures = get_fixtures()

    def test_list_topics(self):
        client = APIClient()
        topics = Topics.objects.all()
        response = client.get(reverse('topics:api:list'))
        self.assertEqual(200, response.status_code)
        self.assertEqual(topics.count(), len(response.data))

    def test_create_topics(self):
        client = APIClient()
        topics_id = Topics.objects.first().id
        data = {
            'title': 'test'
        }
        response = client.post(reverse('topics:api:list'), data, format='json')
        self.assertEqual(201, response.status_code)
        topics = Topics.objects.last()
        self.assertEqual(topics.id, response.data['id'])
        self.assertEqual(topics.title, 'test')
        
    def test_update_topics(self):
        client = APIClient()
        topics = Topics.objects.first()
        topics_id = topics.id
        new_title = 'copy of ' + topics.title
        data = {
            'title': new_title
        }
        response = client.put(reverse('topics:api:detail', args=[topics.id]), data, format='json')
        self.assertEqual(200, response.status_code)
        topics = Topics.objects.filter(title=new_title)
        self.assertTrue(topics.exists())
        self.assertEqual(topics_id, response.data['id'])
        
    def test_delete_topics(self):
        client = APIClient()
        topics = Topics.objects.first()
        topics_id = topics.id
        response = client.delete(reverse('topics:api:detail', args=[topics.id]))
        self.assertEqual(204, response.status_code)
        self.assertFalse(Topics.objects.filter(pk=topics_id).exists())
