"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.urls import include
from the_chatbot import views as the_chatbot_views

urlpatterns = [
    path('index/', the_chatbot_views.index, name='index'),
     path('the_chatbot/', include('the_chatbot.urls')),
    path('admin/', admin.site.urls),
    path('logout/',the_chatbot_views.user_logout, name='logout'),
    path('special/',the_chatbot_views.special,name='special')
]