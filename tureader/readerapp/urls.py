from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^export/xls/$', views.export_page_xls, name='export_page_xls'),
    re_path(r'^export/xls/k$', views.export_all_xls, name='export_all_xls')
] 