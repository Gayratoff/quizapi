from django.contrib import admin
from myfiles.models import *
# Register your models here.


class AdminM(admin.ModelAdmin):
    list_display = ['id','photo','UTC']

admin.site.register(photo, AdminM)