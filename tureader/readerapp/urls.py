from django.urls import path
from . import views
from .views import GeneratePDF

urlpatterns = [
    path('', views.index, name='index'),
    path('test/',views.test,name='test'),
    path('edit/',views.editpage,name='editpage'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('edit/back',views.index,name ='index'),
    path('pdf',GeneratePDF.as_view()),
    path('search/',views.search.as_view(),name='search')
] 