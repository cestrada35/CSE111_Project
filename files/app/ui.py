from django.urls import path

from . import ui_view

urlpatterns = [
    path('', ui_view.home)
]