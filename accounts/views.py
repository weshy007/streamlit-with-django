from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes

from .models import User


# Create your views here.
@api_view(('POST',))
@permission_classes([AllowAny])
def api_getToken(request, *args, **kwargs):
    pass


@api_view(('POST',))
@permission_classes([AllowAny])
def api_register_view(request, *args, **kwargs):
    pass
