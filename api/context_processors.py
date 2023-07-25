from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import *
from .models import *
from rest_framework.views import APIView
from superuser.models import *
from member.models import *
# import requests

# Create your views here.
@api_view(['POST'])
def login(request):

    members = LoginSerializer(data=request.data)

    if members.is_valid():
        email = members.data['email']
        password = members.data['password']
        role = members.data['role']

        if role == "admin":
            pass
        elif role == "member":
            print(email)
            print(password)

        return Response(members.data)
    else:
        return Response(members.errors, status=status.HTTP_400_BAD_REQUEST)  

