from rest_framework import serializers
from django.contrib import admin
admin.autodiscover()
from myfiles.models import *

class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = photo
        fields = ('id','photo','UTC')