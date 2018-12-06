from django.shortcuts import render
from django.http import HttpResponse
from .models import System_lens_135, System_lens_medium, Component, Formula
from rest_framework import viewsets, generics
from .serializers import System_135Serializer, MediumSerializer, ComponentSerializer, FormulaSerializer


#class System_lens_135ViewSet(viewsets.ModelViewSet):
    #queryset = System_lens_135.objects.all()
   # serializer_class = System_135Serializer

#class System_lens_mediumViewSet(viewsets.ModelViewSet):
 #   queryset = System_lens_medium.objects.all()
  #  serializer_class = MediumSerializer

class System_lens_135ViewSet(viewsets.ModelViewSet):
    queryset = System_lens_135.objects.all()
    serializer_class = System_135Serializer

class System_lens_mediumViewSet(viewsets.ModelViewSet):
    queryset = System_lens_medium.objects.all()
    serializer_class = MediumSerializer

class SystemlensMediumList(generics.ListCreateAPIView):
    queryset = System_lens_medium.objects.all()
    serializer_class = MediumSerializer

class Systemlens135List(generics.ListCreateAPIView):
    queryset = System_lens_135.objects.all()
    serializer_class = System_135Serializer

class ComponentList(generics.ListCreateAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

class Component_List(viewsets.ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

class FormulaList(generics.ListCreateAPIView):
    queryset = Formula.objects.all()
    serializer_class = FormulaSerializer

class Formula_List(viewsets.ModelViewSet):
    queryset = Formula.objects.all()
    serializer_class = FormulaSerializer


#def index(request):
   # return HttpResponse(request, 'frontend/index.html')
#def index(request):
#    return HttpResponse("Hello world. You're at the configurator index.")




