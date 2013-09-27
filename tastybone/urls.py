from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'balance.views.index', name='home'),
    # url(r'^tastybone/', include('tastybone.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)



from tastypie.api import Api

from balance.api import OperationResource

v1_api = Api(api_name='api')
v1_api.register(OperationResource())
urlpatterns += patterns('',
    (r'', include(v1_api.urls)),
)

