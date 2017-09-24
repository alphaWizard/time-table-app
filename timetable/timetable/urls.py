
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from routineapp import views
#from django.conf.urls import path, re_path


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^routineapp/(?P<string>\w+)/$'
    url(r'^routineapp/(?P<dayvalue>[a-z]+)/(?P<periodvalue>[1-9])/',views.routinedata.as_view() ),
]


urlpatterns=format_suffix_patterns(urlpatterns)

#?P<dayvalue>\w+)/(?P<periodvalue>[1-9])
