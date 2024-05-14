from django.contrib import admin
from django.urls import include, path

from . import views
from lettings import urls as lettings_urls
from profiles import urls as profiles_urls
# from lettings import views as lettings_views
# from profiles import views as profiles_views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include(lettings_urls)),
    path('profiles/', include(profiles_urls)),
    # path('lettings/', include('lettings.urls')),
    # path('profiles/', include('profiles.urls')),

    # path('lettings/', views.lettings_index, name='lettings_index'),
    # path('lettings/<int:letting_id>/', views.letting, name='letting'),
    # path('profiles/', views.profiles_index, name='profiles_index'),
    # path('profiles/<str:username>/', views.profile, name='profile'),

    path('admin/', admin.site.urls),
]


# polls/urls.py¶
# from django.urls import path
# from . import views

# app_name = "polls"
# urlpatterns = [
#     path("", views.IndexView.as_view(), name="index"),
#     path("<int:pk>/", views.DetailView.as_view(), name="detail"),
#     ...,
# ]

# urls.py¶
# from django.urls import include, path

# urlpatterns = [
#     path("polls/", include("polls.urls")),
# ]
