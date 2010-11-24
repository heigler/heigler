#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.test import TestCase
from django.template import Template, Context
from heigler.core.models import Presentation, Work, SocialNetwork

class PresentationTagsTest(TestCase):
    
    fixtures = ['presentations.json']
    
    def test_render_presentation(self):
        instance = Presentation.objects.filter(type='home')[0]
        
        t = Template('''{% load core_tags %}
        {% render_presentation instance.language instance.type %} 
        ''')
        c = Context({'instance': instance})
        content = t.render(c)
        
        self.assertTrue(instance.title in content)
        self.assertTrue(instance.content in content)


class WorkTagsTest(TestCase):
    
    fixtures = ['works.json']
    
    def test_work_list(self):        
        t = Template('''{% load core_tags %}
        {% work_list %}''')
        c = Context({})
        content = t.render(c)
        
        expected_queryset = Work.objects.all()
        for item in expected_queryset:
            self.assertTrue(item.title in content)
            self.assertTrue(item.get_absolute_url() in content)
            

class SocialNetworkTagsTest(TestCase):
    
    fixtures = ['socialnetworks.json']
    
    def test_socialnetwork_list(self):
        t = Template('''{% load core_tags %}
        {% socialnetwork_list %}''')
        c = Context({})
        content = t.render(c)
        
        expected_queryset = SocialNetwork.objects.all()
        for item in expected_queryset:
            self.assertTrue(item.link in content)
            self.assertTrue(item.get_media_url() in content)
            self.assertTrue(item.get_name() in content)           
  
