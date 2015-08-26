from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'thermostat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^thermostat/', include('ThermoApp.urls', namespace='ThermoApp')),
    url(r'^admin/', include(admin.site.urls)),
]
