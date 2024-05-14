from django.urls import path

from . import views

app_name = 'lettings'
urlpatterns = [
    path('lettings/', views.index, name='lettings_index'),
    path('lettings/<int:letting_id>/', views.letting, name='letting'),
]
