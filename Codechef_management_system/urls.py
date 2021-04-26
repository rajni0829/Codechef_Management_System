"""Codechef_management_system URL Configuration

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

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from Codechef_management_system import settings
from codechef_management_app import views

urlpatterns = [
    path("",views.showDemoPage,name="demo"),
    path('admin/', admin.site.urls),
    path('codechef_management_app/register',views.register,name="register"),
    path('codechef_management_app/login',views.login,name="login"),
    path("codechef_management_app/codechef_management_app/logout",views.logoutt,name="logout"),
    path("codechef_management_app/events",views.events,name="events" ),
    path("codechef_management_app/executive_register",views.executive_register,name="executive_register" ),



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

