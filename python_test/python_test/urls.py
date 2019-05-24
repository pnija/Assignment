"""python_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from .views import ClientHome, SearchClients, ClientDetails, AddClientDetails, EditClientDetails, GetEditClientDetails

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('', ClientHome.as_view(), name="home"),
    path('search', SearchClients.as_view(), name='search_clients'),
    path('client', ClientDetails.as_view(), name='client_details'),
    path('client/add', AddClientDetails.as_view(), name='add_client'),
    path('client/edit', EditClientDetails.as_view(), name='edit_client'),
    path('client/get_edit_details', GetEditClientDetails.as_view(), name="get_edit_details"),
]
