from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from .serializers import UserSerializer, LoginSerializer, RegisterSerializer
from .authentication import generate_jwt_token
from .models import UserProfile


class AuthViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=["post"])
    def login(self, request):
        """Login endpoint"""
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        token = generate_jwt_token(user)

        user_data = UserSerializer(user).data

        return Response(
            {
                "access_token": token,
                "user": user_data,
            },
            status=status.HTTP_200_OK,
        )

    @action(detail=False, methods=["post"])
    def register(self, request):
        """Register new user"""
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        token = generate_jwt_token(user)
        user_data = UserSerializer(user).data

        return Response(
            {
                "access_token": token,
                "user": user_data,
            },
            status=status.HTTP_201_CREATED,
        )

    @action(detail=False, methods=["get"], permission_classes=[IsAuthenticated])
    def me(self, request):
        """Get current user"""
        user_data = UserSerializer(request.user).data
        return Response(user_data, status=status.HTTP_200_OK)
