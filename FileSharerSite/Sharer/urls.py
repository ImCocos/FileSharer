from django.urls import path, include
from Sharer.views import *

urlpatterns = [
    path('', index, name='home'),
    path('files/page-<int:page>/', index, name='files-page'),
    path('share', share, name='share'),
]
