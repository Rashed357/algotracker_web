from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This line connects our tracker app to the main website
    path('', include('tracker.urls')), 
]