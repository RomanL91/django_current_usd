from django.contrib import admin
from django.urls import path, include

from app_stock_observer.urls import urlpatterns_get_current

urlpatterns = [
    path('', include(urlpatterns_get_current)),
    path('admin/', admin.site.urls),
]
