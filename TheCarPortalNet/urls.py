"""TheCarPortalNet URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from affiliate.views import get_carportal

urlpatterns = [
    path('', get_carportal),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('events/', include('Event.urls')),
    path('store/', include('Store.urls')),
    path('cart/', include('Cart.urls')),
    path('sale/', include('Enquiry.urls')),
    path('automart/', include('Automart.urls'))
]

admin.site.site_header = 'The Car Portal Admin Dashboard'
admin.site.index_title = 'Car Portal Administration'
admin.site.site_title = 'Admin Dashboard'