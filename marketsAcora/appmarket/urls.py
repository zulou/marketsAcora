from django.conf.urls import url
from django.contrib import admin
from . import views



urlpatterns = [
    url(r'^index/', views.index),
    url(r'^admin/', views.admin),
    url(r'^vouchers/', views.vouchers),
    url(r'^id_voucher/', views.last_id_voucher),
    url(r'^imprimir/(\d+)/$', views.imprimir, name='imprimir'),
    url(r'^water_reading/', views.water_reading, name='water_reading'),
    url(r'^electricity_reading/', views.water_reading, name='electricity_reading'),

]