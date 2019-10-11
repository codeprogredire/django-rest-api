from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('status/',include('status.urls')),
    path('accounts/',include('accounts.urls')),
]
