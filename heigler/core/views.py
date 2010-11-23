#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic.list_detail import object_detail
from heigler.core.models import Presentation

def presentation_detail(request, language, type, object_id):
    qs = Presentation.objects.filter(language=language, type=type)
    response = object_detail(request, queryset=qs, object_id=object_id)
    return response

def work_detail(request, language, slug):
    pass
