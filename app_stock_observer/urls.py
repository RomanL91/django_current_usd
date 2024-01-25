from django.urls import path

from app_stock_observer.views import RootView, GetCurrentUsd


urlpatterns_get_current = [
    path('', RootView.as_view(), name="root"),
    path('get-current-usd/', GetCurrentUsd.as_view(), name="get_current_usd"),
]
