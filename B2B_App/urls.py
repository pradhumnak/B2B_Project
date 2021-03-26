from django.conf.urls import url
from B2B_App import views
from django.urls import path



urlpatterns = [
    path('',views.index, name='index'),
    path(r'fdrpage/',views.fdrpage, name='fdrpage')
]

