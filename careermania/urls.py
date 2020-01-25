from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('webapp.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/', include('webapi.urls')),
    path('admin/', admin.site.urls),
]
