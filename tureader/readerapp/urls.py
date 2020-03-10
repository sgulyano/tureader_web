# from django.urls import path, re_path
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^export/xls/$', views.export_page_xls, name='export_page_xls'),
    url(r'^export/xls/k$', views.export_all_xls, name='export_all_xls')
    # path('', views.index, name='index'),
    # re_path(r'^export/xls/$', views.export_page_xls, name='export_page_xls'),
    # re_path(r'^export/xls/k$', views.export_all_xls, name='export_all_xls')
] 