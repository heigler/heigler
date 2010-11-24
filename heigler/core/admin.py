#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from heigler.core.models import Presentation, SocialNetwork, Work

admin.site.register(Presentation)
admin.site.register(SocialNetwork)
admin.site.register(Work)
