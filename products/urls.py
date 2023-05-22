from django.urls import path
from site2 import views
from products import views

urlpatterns = [
    #path('site2/', views.site2, name='site2'),
    path(r'^product/(?P<product_id>\w+)/$', views.product, name='product'),
    path(r'^product/(?P<product_id>\w+)/$', views.feedback, name='feedback'),
]