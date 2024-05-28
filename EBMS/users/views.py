from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError as DRFValidationError
from .models import User
from .serializers import UserSerializer, LoginSerializer
from .permissions import IsSelfOrAdminUser


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        if request.user.is_authenticated:
            if request.user.is_staff:
                queryset = self.get_queryset()
            else:
                queryset = User.objects.filter(id=request.user.id)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            # Check if the email is already in use
            if User.objects.filter(email=email).exists():
                raise DRFValidationError({"email": ["User with this email already exists."]})
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSelfOrAdminUser, IsAuthenticated]


class WhoAmIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        data = {
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "title": user.title,
            "is_active": user.is_active,
            "is_staff": user.is_staff,
            "is_superuser": user.is_superuser,
        }
        return Response(data)


class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = request.data.get('email')
            password = request.data.get('password')

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                user_serializer = UserSerializer(user)
                return Response({'token': token.key, 'user': user_serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
