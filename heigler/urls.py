from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'base.html'}),    
    (r'^admin/', include(admin.site.urls)),
    
    # core routes
    url(r'^presentations/(?P<language>[-\w]+)/(?P<type>[-\w]+)/(?P<object_id>\d+)/$', 'heigler.core.views.presentation_detail', 
        name='core_presentation_detail'),
    url(r'^works/(?P<language>[-\w]+)/(?P<slug>[-\w+]+)/$', 'heigler.core.views.work_detail', name='core_work_detail'),
    
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
