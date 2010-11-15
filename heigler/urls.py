from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'base.html'}),
    
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
