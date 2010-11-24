#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

class ContactForm(forms.Form):
    name = forms.CharField(label=_('name'), max_length=50)
    email = forms.EmailField(label=_('e-mail'))
    subject = forms.CharField(label=_('subject'), max_length=100)
    content = forms.CharField(label=_('content'), widget=forms.Textarea)
