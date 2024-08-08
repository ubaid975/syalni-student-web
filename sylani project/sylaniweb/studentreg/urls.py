from django.urls import path
from . import views
urlpatterns = [
    
    path('register/',views.register),
    path('data/',views.data),
    path('result/',views.result),
]