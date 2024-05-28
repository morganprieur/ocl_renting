from django.contrib import admin
from django.urls import include, path, re_path

from django.conf import settings
from django.views.static import serve

from . import views

handler404 = 'oc_lettings_site.views.page_not_found'
handler500 = 'oc_lettings_site.views.server_error'

urlpatterns = [
    path('admin/', admin.site.urls),

    path('lettings/', include('lettings.urls', namespace='lettings')),
    path("profiles/", include('profiles.urls', namespace='profiles')),
    path("hello_world/", views.hello_world),

    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('', views.index, name='index'),
]
