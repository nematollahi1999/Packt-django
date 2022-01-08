from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from cstmapp.models import Plist
from cstmapp.serializers import UserSerializer, PlistSerializer
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello Bitch!</h1>")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#APIs
# /cstmhome/

@csrf_exempt
def product_list(request):
    #Get all
    if request.method == 'GET':
        products = Plist.objects.all()
        products_serializer = PlistSerializer(products, many=True)
        return JsonResponse(products_serializer.data, safe=False)

    #Add one
    if request.method == 'POST':
        product_data = JSONParser().parser(request)
        product_serializer = PlistSerializer(data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse(product_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Delete all
    if request.method == 'DELETE':
        Plist.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
def product_detail(request, pk):
    try:
        product = Plist.objects.get(pk=pk)
    except Plist.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    #Retreive one
    if request.method == 'GET':
        product_serializer = PlistSerializer(product)
        return JsonResponse(product_serializer.data)

    #Update one record
    if request.method == 'PUT':
        product_data = JSONParser().parser(request)
        product_serializer = PlistSerializer(product, data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse(product_serializer.data)
        return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Delete one record
    if request.method == 'DELETE':
        product.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)