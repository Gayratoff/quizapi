from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from rest_framework.generics import ListAPIView,DestroyAPIView,RetrieveUpdateAPIView,CreateAPIView
from myfiles.models import  *
from myfiles.Serializer import *

# Create your views here.

# PHOTO ADS API

class IndexView(TemplateView):
    template_name = 'index.html'

class ads_api(ListAPIView):
    queryset = photo.objects.all()
    serializer_class = PhotoSerializer

class ads_api_add(CreateAPIView):
    queryset = photo
    serializer_class = PhotoSerializer

class ads_api_delete(DestroyAPIView):
    queryset = photo
    serializer_class = PhotoSerializer

class ads_api_update(RetrieveUpdateAPIView):
    queryset = photo
    serializer_class = PhotoSerializer

# PHOTO ADS API