"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from myapp import views

urlpatterns = [
    path('',views.index),
	path('admin/', admin.site.urls),
    path('gogo/', views.pylinkweb),
    path('fv/', views.deposits),
    path('result/', views.result),

    path('company/',views.company),
    path('company/insert/',views.insert),
    path('do_insert/',views.do_insert),
    path('company/detail/<int:stockid>/',views.detail),
    path('company/update/<int:stockid>/',views.update),
    path('do_update/',views.do_update),
    path('company/delete/<int:stockid>/',views.delete),
    path('do_delete/',views.do_delete),

]
