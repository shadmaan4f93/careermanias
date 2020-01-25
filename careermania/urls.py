from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('coaching/', include('coachings.urls')),
    path('admin/', admin.site.urls),
]
