from django.urls import path
from .views import *
urlpatterns = [
    path('', post_list, name='post_list'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail')
]