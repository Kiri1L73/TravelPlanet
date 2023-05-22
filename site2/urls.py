from django.urls import path
from site2 import views

urlpatterns = [
    path('', views.home, name='home'),
    path('site2/', views.site2, name='site2'),
]