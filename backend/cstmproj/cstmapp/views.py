from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from cstmapp.serializers import UserSerializer
from rest_framework import viewsets

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello Bitch!</h1>")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer