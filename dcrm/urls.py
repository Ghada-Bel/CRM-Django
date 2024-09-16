
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('website.urls')),
    path('gest_cmd/',include('gest_cmd.urls')),
    path('sales/',include('sales.urls')),
]
