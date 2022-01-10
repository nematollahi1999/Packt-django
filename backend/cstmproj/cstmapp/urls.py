#from django.db import router
from django.urls import path, include, re_path
#from django.conf.urls import url
#from django.urls.conf import include
from . import views
from rest_framework import routers


#router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)

urlpatterns = [
    #path('' ,views.index, name='index'),
    #path('',include(router.urls))
    re_path(r'^$',views.product_list),
    re_path(r'^(?P<pk>[0-9]+)$', views.product_detail)
]