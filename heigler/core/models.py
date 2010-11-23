#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class Presentation(models.Model):
    
    TYPE_CHOICES = (('home', _('Home')),
                    ('about', _('About')))
    
    title = models.CharField(_('title'), max_length=150)
    type = models.CharField(_('type'), max_length=30, choices=TYPE_CHOICES)
    content = models.TextField(_('content'))
    language = models.CharField(_('language'), max_length=10, choices=settings.LANGUAGES)
    
    class Meta:
        verbose_name = _('presentation')
        verbose_name_plural = _('presentations')
        unique_together = (('type', 'language'),)
        
    def __unicode__(self):
        return self.title
        
    @models.permalink
    def get_absolute_url(self):
        return ('core_presentation_detail', [self.language, self.type])
        

class SocialNetwork(models.Model):
    
    TYPE_CHOICES = (('facebook.jpg', 'Facebook'),
                    ('orkut.jpg', 'Orkut'),
                    ('twitter.jpg', 'Twitter'),
                    ('github.png', 'GitHub'))
                    
    type = models.CharField(_('type'), max_length=30, choices=TYPE_CHOICES, unique=True)
    link = models.URLField(_('link'), verify_exists=False)
    
    class Meta:
        verbose_name = _('social network')
        verbose_name_plural = _('social networks')
        
    def __unicode__(self):
        return self.type
        
    def get_media_url(self):
        return '%sstyle/%s' %(settings.MEDIA_URL, self.type)
        
        
class Work(models.Model):
    
    title = models.CharField(_('title'), max_length=150)
    start_date = models.DateField(_('start date'))
    end_date = models.DateField(_('end date'), null=True, blank=True)
    company_name = models.CharField(_('company name'), max_length=100, null=True, blank=True)
    content = models.TextField(_('content'))
    image = models.ImageField(_('image'), upload_to='core/work/image')
    language = models.CharField(_('language'), max_length=10, choices=settings.LANGUAGES)
    
    class Meta:
        verbose_name = _('work')
        verbose_name_plural = _('works')
        
    def __unicode__(self):
        return self.title        
    

