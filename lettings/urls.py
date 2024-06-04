from django.urls import path

from . import views

# print('lettings/urls')

app_name = 'lettings'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:letting_id>/', views.letting, name='letting'),
]
