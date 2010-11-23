#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from django.test import TestCase
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db.utils import IntegrityError
from heigler.core.models import Presentation, SocialNetwork, Work

class PresentationModelTest(TestCase):
    
    fixtures = ['presentations.json']
    
    def create_instance(self, **kwargs):
        default_options = {'title': 'Test title', 'type': 'something', 'content': 'test content',
                           'language': 'pt_BR'}
        default_options.update(kwargs)
        return Presentation.objects.create(**default_options)        
    
    def test_creation(self):
        instance = self.create_instance()
        self.assertTrue(instance.pk, 'could not create a presentation')
        
    def test_absolute_url_method(self):
        instance = Presentation.objects.all()[0]
        url = getattr(instance, 'get_absolute_url', lambda: False)()
        expected_url = reverse('core_presentation_detail', args=[instance.language, instance.type])
        
        self.assertTrue(url, 'method not implemented')
        self.assertEqual(url, expected_url)
        
    def test_unique_rules(self):
        first_instance = self.create_instance()
        
        # same language and type are not allowed
        self.assertRaises(IntegrityError, self.create_instance)
        

class SocialNetworkModelTest(TestCase):
    
    fixtures = ['socialnetworks.json']
    
    def test_creation(self):
        instance = SocialNetwork.objects.create(type='github', link='http://facebook.com')
        self.assertTrue(instance.pk, 'could not create a socialnetwork')
        
    def test_media_method(self):
        instance = SocialNetwork.objects.all()[0]
        media_url = getattr(instance, 'get_media_url', lambda: False)()
        expected_media_url = '%sstyle/%s' %(settings.MEDIA_URL, instance.type)
        
        self.assertTrue(media_url, 'method not implemented')
        self.assertEqual(media_url, expected_media_url)
        
        
class WorkModelTest(TestCase):
    
    def test_creation(self):
        today = datetime.today()
        tomorrow = today + timedelta(days=1)
        instance = Work.objects.create(title='Test title', start_date=today, end_date=tomorrow,
                                       company_name='Test company', content='Test content', image='test.jpg',
                                       language='en-us')  
                                       
        self.assertTrue(instance.pk, 'could not create a work')
        
        
        
