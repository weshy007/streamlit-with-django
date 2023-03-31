from django.urls import path

from . import views

urlpatterns = [
    path('api_register/', views.api_register_view),
    path('api_auth/', views.api_getToken),
]