from django.urls import path
from .views import TestClass

urlpatterns = [
    path('get-test/', TestClass.as_view())
]