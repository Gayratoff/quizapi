"""djangofiles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from myfiles.views import *
from django.conf.urls.static import static
from djangofiles import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/quiz-auth/', include('dj_rest_auth.urls')),
    path('api/v1/quiz-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('', IndexView.as_view()),
    path('api-ads/view/',ads_api.as_view()),
    path('api-ads/add/',ads_api_add.as_view()),
    path('api-ads/delete/<pk>/',ads_api_delete.as_view()),
    path('api-ads/update/<pk>/',ads_api_update.as_view()),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIAFILE_DIRS)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)