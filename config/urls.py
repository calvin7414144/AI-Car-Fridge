"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import include, path

from .views import frontend_page, set_admin_language

admin.site.site_header = 'AI Car Fridge Admin'
admin.site.site_title = 'AI Car Fridge Admin'
admin.site.index_title = 'Home'

urlpatterns = [
    path('', frontend_page, {'page': 'index'}, name='frontend_home'),
    path('product/', frontend_page, {'page': 'product'}, name='frontend_product'),
    path('factory/', frontend_page, {'page': 'factory'}, name='frontend_factory'),
    path('custom/', frontend_page, {'page': 'custom'}, name='frontend_custom'),
    path('contact/', frontend_page, {'page': 'contact'}, name='frontend_contact'),
    path('admin/language/<str:language_code>/', set_admin_language, name='set_admin_language'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
]
