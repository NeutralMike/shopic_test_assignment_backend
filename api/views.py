from django.contrib.auth import authenticate, login

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
        if username is None or password is None:
            return Response(
                {"detail": "Please enter both username and password"},
                status=400
            )
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"detail": "Success"})
        return Response(
            {"detail": "Invalid credentials"},
            status=400,
        )

