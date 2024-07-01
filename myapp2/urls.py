from django.urls import path
from myapp2.views import index, total_in_db, total_in_view, total_in_template

urlpatterns = [
path('', index, name='index'),
path('example1/', total_in_db, name='total_in_db'),
path('example2/', total_in_view, name='total_in_db'),
path('example3/', total_in_template, name='total_in_db'),
]