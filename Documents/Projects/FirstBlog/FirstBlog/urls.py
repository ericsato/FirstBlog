from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog.views.home', name='home'),
    url(r'^about/', 'blog.views.about', name='about'),
    url(r'^radsuggestion/', 'blog.views.radsuggestion', name='radsuggestion'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
