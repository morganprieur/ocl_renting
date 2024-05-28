from django.contrib import admin
from django.urls import include, path, re_path

from django.conf import settings
from django.views.static import serve

from . import views

handler404 = "oc_lettings_site.views.page_not_found"
# handler500 = "oc_lettings_site.views.server_error"
handler500 = views.server_error

urlpatterns = [
    path('admin/', admin.site.urls),

    path('lettings/', include('lettings.urls', namespace='lettings')),
    path("profiles/", include('profiles.urls', namespace='profiles')),
    path("hello_world_error/", views.hello_world_error),

    re_path(r'ŝtatic/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    # re_path(r'ŝtatic/(?p<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('', views.index, name='index'),
]
