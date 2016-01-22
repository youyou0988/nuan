from django.conf.urls import patterns, include, url

from django.contrib import admin
import users
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nuan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/', 'users.views.index'),
    url(r'^privacy/', 'users.views.privacy'),
    url(r'^condition/', 'users.views.condition'),
    url(r'^register/', 'users.views.register'),
)
