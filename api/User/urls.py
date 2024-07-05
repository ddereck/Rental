from django.urls import path, include
from .Views.views import *
from .Views.UserViews import *
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'drivers', DriverViewSet)


urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('refresh-token', UserTokenRefreshView.as_view(), name='token_refresh'),
    path('logout', Logout.as_view(), name='logout'),


    # Users
    path('users', users, name='users'),
    path('user/<uuid:id>', userById, name='user'),
    path('current-user', user, name='current-user'),
    path('register', register, name='register'),
    path('update/<uuid:user_id>', updateUser, name='update-user'),
    path('update-password/<uuid:id>', updatePassword, name='update-password'),
    path('reset-password', resetPassword, name='reset-password'),
    path('update-profile-image/<uuid:id>', updatePhotoProfile, name='update-profile-image'),

    path('', include(router.urls)),
]
