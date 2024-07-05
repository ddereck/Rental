from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from ..models import Users
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from ..mail_config import *
from ..serializers import UsersSerializer, UsersSerializerAdd
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
import string
import random
from django.shortcuts import get_object_or_404
from AUTO.Helper import formatUserPictureUrl
from django.db.models import Q
from AUTO.Helper import *

def generate_password():
    """
    Générer un nouveau mot de passe aléatoire
    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(8))

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def user(request):
    user = request.user
    serializer = UsersSerializer(user)
    formatData = serializer.data
    formatData['photo'] = request.build_absolute_uri(serializer.data['photo']) if serializer.data['photo'] else None
    return Response(formatData)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def userById(request, id):
    user = Users.objects.get(id=id)
    serializer = UsersSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def users(request):
    users = Users.objects.all()
    serializer = UsersSerializer(users, many=True)
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([AllowAny])
@transaction.atomic
def register(request):
    request.data['username'] = request.data.get('email') if not request.data.get('email') else request.data.get('phone')
    newPassword = request.data['password']
    request.data['password'] = make_password(newPassword)
    serializer = UsersSerializerAdd(data=request.data)
    if serializer.is_valid():
        serializer.validated_data['photo'] = saveOrRemoveFile(image_file=request.FILES['photo'], location=f'media/images/') if 'photo' in request.FILES else None
        user = serializer.save()

        sendResetPasswordEmail(user.email, newPassword, user)
        return Response({
            'message': 'Compte créé avec succès',
            }, status=201)
    else:
        return Response({
            'message': 'Cannot create user',
            'error': serializer.errors,
            }, status=400)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@transaction.atomic
def updateUser(request, user_id):
    try:
        user = Users.objects.get(id=user_id)
    except Users.DoesNotExist:
        return Response({'message': 'User not found'}, status=404)

    serializer = UsersSerializerAdd(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.validated_data['photo'] = saveOrRemoveFile(image_file=request.FILES['photo'], old_file=user.photo, location=f'media/images/') if 'photo' in request.FILES else None
        serializer.save()
        return Response({'message': 'User updated successfully'}, status=200)
    else:
        return Response({
            'message': 'Cannot update user',
            'error': serializer.errors
            }, status=422)

    
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def updatePassword(request, id):
    user = Users.objects.get(id=id)
    if not user:
        return Response({'message': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)

    old_password = request.data.get('password')
    if not check_password(old_password, user.password):
        return Response({'message': 'Le mot de passe actuel est incorrect'}, status=status.HTTP_400_BAD_REQUEST)

    new_password = request.data.get('new_password')
    user.password = make_password(new_password)
    user.save()
    
    return Response({
        'message': 'Password updated successfully',
        }, status=status.HTTP_200_OK) 

@api_view(['POST'])
@permission_classes([AllowAny])
def resetPassword(request):
    """
    Réinitialiser le mot de passe d'un utilisateur
    """
    email = request.data.get('email')
    try:
        user = Users.objects.get(email=email)
        new_password = generate_password()
        user.password = make_password(new_password)
        user.save()
        sendResetPasswordEmail(user.email, new_password, user)
        return Response({
            'message': 'An email has been sent to you with instructions to reset your password.'
        }, status=200)
    except ObjectDoesNotExist:
        return Response({'message': 'User not found'}, status=404)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def updatePhotoProfile(request, id):
    user = get_object_or_404(Users, id=id)
    serializer = UsersSerializerAdd(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.validated_data['photo'] = saveOrRemoveFile(image_file=request.FILES['photo'], old_file=user.photo, location=f'media/profiles/') if 'photo' in request.FILES else None
        serializer.save()
        return Response({'message': 'Photo de profil modifiée avec succès.'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
