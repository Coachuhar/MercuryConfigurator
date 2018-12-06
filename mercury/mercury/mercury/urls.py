"""mercury URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from configurator import views 
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'System_lens_135', views.System_lens_135ViewSet)
router.register(r'System_lens_medium', views.System_lens_mediumViewSet) 
router.register(r'Components', views.Component_List)
router.register(r'Formulas', views.Formula_List)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('configurator.urls')),
    path('', include('frontend.urls')),
    url(r'^', include(router.urls)),
   
]
