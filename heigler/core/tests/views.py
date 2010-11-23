#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from heigler.core.models import Presentation

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
