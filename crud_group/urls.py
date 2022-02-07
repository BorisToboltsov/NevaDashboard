"""NevaSeason URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.urls import path, include
from crud_group.views import add_group, detail_group

app_name = 'crud_group'

urlpatterns = [
    # path('add/', AddGroup.as_view(), name='add'),
    path('add/', add_group, name='add'),
    path('detail_group/<int:pk>/', detail_group, name='detail_group'),
    ]
