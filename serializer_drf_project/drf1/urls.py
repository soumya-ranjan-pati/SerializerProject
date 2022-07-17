"""drf1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from myapp import views
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Insert/',csrf_exempt(views.ProductOperation.as_view())),
    path('showall/',csrf_exempt(views.showall.as_view())),
    path('single/',csrf_exempt(views.singlerecord.as_view())),
    path('update/',csrf_exempt(views.Updaterecord.as_view())),
    path('delete/',csrf_exempt(views.Deleterecord.as_view())),
]
