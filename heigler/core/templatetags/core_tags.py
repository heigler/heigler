#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.template import Library
from heigler.core.models import Presentation, Work, SocialNetwork

register = Library()

@register.inclusion_tag('core/inclusion_tags/render_presentation.html')
def render_presentation(language, type):
    try:
        instance = Presentation.objects.get(language=language, type=type)
    except Presentation.DoesNotExist:
        return {'object': None}
    return {'object': instance}
    

@register.inclusion_tag('core/inclusion_tags/work_list.html')
def work_list():
    qs = Work.objects.all().order_by('start_date')
    return {'object_list': qs}
    
    
@register.inclusion_tag('core/inclusion_tags/socialnetwork_list.html')
def socialnetwork_list():
    qs = SocialNetwork.objects.all().order_by('type')
    return {'object_list': qs}
