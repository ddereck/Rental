from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from ..serializers import UsersSerializer, DriverSerializer
from ..models import Users, Drivers
from django.contrib.auth import logout
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenRefreshView
from AUTO.Helper import *
from django.db.models import Q
from rest_framework import viewsets

class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UsersSerializer

    def post(self, request):
        email_or_phone = request.data.get('email_or_phone')
        password = request.data.get('password')

        if email_or_phone is None:
            return Response({'errors': 'Please provide an email or phone number.'}, status=status.HTTP_400_BAD_REQUEST)

        user = self.get_user(email_or_phone)
        
        if user is None or not user.check_password(password) or not user.is_active:
            return Response({'errors': 'Incorrect email/phone or password!'}, status=status.HTTP_400_BAD_REQUEST)

        refresh = RefreshToken.for_user(user)
        user.token = str(refresh.access_token)
        user.save()

        response = {
            'message': 'Welcome! Successfully connected.',
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': self.serializer_class(user).data
        }
        return Response(response, status=status.HTTP_200_OK)

    def get_user(self, email_or_phone):
        try:
            return Users.objects.get(
                Q(email=email_or_phone) | Q(phone_number=email_or_phone)
            )
        except Users.DoesNotExist:
            return None


class UserTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            user = self.user
            return Response({
                'refresh': str(response.data.get('refresh')),
                'access': str(response.data.get('access')),
                'user': {
                    'id': str(user.id),
                    'email': user.email,
                    'phone': user.phone,
                }
            })
        return response

class Logout(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Drivers.objects.all()
    serializer_class = DriverSerializer