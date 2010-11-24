#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from heigler.core.models import Presentation, Work

class PresentationViewTest(TestCase):
    
    fixtures = ['presentations.json']
    
    def test_detail_response(self):
        instance = Presentation.objects.all()[0]
        url = instance.get_absolute_url()
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/presentation_detail.html')
        self.assertContains(response, instance.title)
        self.assertContains(response, instance.content)
        
class WorkViewTest(TestCase):
    
    fixtures = ['works.json']

    def test_detail_response(self):
        instance = Work.objects.all()[0]
        url = instance.get_absolute_url()
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/work_detail.html')
        self.assertContains(response, instance.title)
        self.assertContains(response, instance.company_name)
        self.assertContains(response, instance.content)
        self.assertContains(response, instance.url)
        
    def test_list_response(self):
        url = reverse('core_work_list', args=['en-us'])
        response = self.client.get(url)
        expected_queryset = Work.objects.filter(language='en-us').order_by('title')
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/work_list.html')
        
        for item in expected_queryset:
            self.assertContains(response, item.title)
            self.assertContains(response, item.get_absolute_url())
