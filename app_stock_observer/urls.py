from django.urls import path

from app_stock_observer.views import MyView


urlpatterns_get_current = [
    path('get-current-usd/', MyView.as_view(), name="my-view"),
]