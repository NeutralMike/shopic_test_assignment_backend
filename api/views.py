from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication


class AuthCheck(APIView):
    authentication_classes = [SessionAuthentication]

    def get(self, request):
        return Response({'detail': 'You\'re Authenticated'})


class LoginView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response(
                {"general": "Please enter both username and password"},
                status=400
            )
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(
                {"username": "The username is incorrect"},
                status=400
            )
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"detail": "Success"})
        return Response(
            {"password": "The password is incorrect"},
            status=400,
        )

