from django.db import IntegrityError
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed

from .models import CustomUser
from .token import get_tokens_for_user
from .serializers import RegistrationSerializer, UserSerializer


class RegistrationAPIView(APIView):

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        created_user = CustomUser.objects.create(
            profile_img=serializer.validated_data.get("profile_img"),
            username=serializer.validated_data.get("username"),
            nickname=serializer.validated_data.get("nickname")
        )
        created_user.set_password(serializer.validated_data.get("password"))
        created_user.save()

        Token.objects.create(user=created_user)

        result = UserSerializer(created_user)
        return Response(data=result.data, status=201)


class LoginAPIView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:

            tokens = get_tokens_for_user(user)

            response = {
                "message": "Login Successfull",
                "token": tokens
            }
            return Response(data=response, status=200)
        else:
            return Response(data={"massage": "Invalid username or password"})




class LogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response({'msg': 'Successfully Logged out'}, status=200)
