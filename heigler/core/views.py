#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.views.generic.list_detail import object_detail, object_list
from django.views.generic.simple import direct_to_template
from django.http import Http404
from heigler.core.models import Presentation, Work

def presentation_detail(request, language, type):
    try:
        instance = Presentation.objects.get(language=language, type=type)
    except Presentation.DoesNotExist:
        raise Http404('presentation not found')
    
    response = direct_to_template(request, extra_context={'object': instance},
                                  template='core/presentation_detail.html')    
    return response


def work_detail(request, language, slug):
    qs = Work.objects.filter(language=language)
    response = object_detail(request, queryset=qs, slug=slug)
    return response


def work_list(request, language):
    qs = Work.objects.filter(language=language).order_by('title')
    response = object_list(request, queryset=qs)
    return response
