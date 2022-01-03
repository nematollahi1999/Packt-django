#from django.db import router
from django.urls import path, include
#from django.urls.conf import include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    #path('' ,views.index, name='index'),
    path('',include(router.urls))
]