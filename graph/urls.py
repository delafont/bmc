from django.conf.urls import patterns, url

from graph import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^response.json/?$', views.json_response, name='json_response'),
    url(r'^newsample.json/?$', views.new_sample, name='new_sample'),
    url(r'^removesample.json/?$', views.remove_sample, name='remove_sample'),
    url(r'^clear.json/?$', views.clear_all_db, name='clear_all_db'),
    url(r'^update_active_table_id/?$', views.update_active_table_id, name='update_active_table_id'),
    url(r'^getfile/(?P<pk>\d+)', views.getfile, name='getfile'),
    url(r'^getimages/(?P<pk>\d+)', views.getimages, name='getimages'),
    #url(r'^sample_file/?$', views.sample_file, name='sample_file'),
    url(r'^doc/?$', views.documentation, name='doc'),
)


#------------------------------------------------------#
# This code was written by Julien Delafontaine         #
# Bioinformatics and Biostatistics Core Facility, EPFL #
# http://bbcf.epfl.ch/                                 #
# webmaster.bbcf@epfl.ch                               #
#------------------------------------------------------#
