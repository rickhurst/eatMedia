from django.conf.urls.defaults import *
from django.core.urlresolvers import reverse
from django.views.generic.simple import direct_to_template



urlpatterns = patterns(
    '',

    (r'^$', 'eatMedia.views.home'),

    (r'^folder/(?P<slug>[\w-]+)', 'eatMedia.views.folder'),

    (r'^cron/ingest/$', 'eatMedia.views.ingest'),
    
    # static maia examples
    #(r'examples/buttons/$', direct_to_template, {'template': 'maia-examples/buttons.html'}),
    #(r'examples/grid/$', direct_to_template, {'template': 'maia-examples/grid.html'}),
    #(r'examples/notifications/$', direct_to_template, {'template': 'maia-examples/notifications.html'}),
    #(r'examples/typography/$', direct_to_template, {'template': 'maia-examples/typography.html'}),


)
