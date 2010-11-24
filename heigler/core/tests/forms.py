#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.test import TestCase
from heigler.core.forms import ContactForm

class ContactFormTest(TestCase):
    
    def test_validation(self):
        form = ContactForm({'name': 'Test name', 'email':'somone@somewhere.com',
                            'subject': 'Test subject', 'content': 'Test content'})
        self.assertTrue(form.is_valid())
    
    
