from django.urls import path

from users.views import UserAuthAPIView, UserConfirmPhoneAPIView, UserDetailAPIView, UserWriteCodeAPIView

urlpatterns = [
    path(
        'login/',
        UserAuthAPIView.as_view(),
        name='login'
    ),
    path(
        'login/confirm/',
        UserConfirmPhoneAPIView.as_view(),
        name='login-confirm'
    ),
    path(
        '<int:pk>/',
        UserDetailAPIView.as_view(),
        name='user-detail'
    ),
    path(
        'add-inviter/<int:pk>/',
        UserWriteCodeAPIView.as_view(),
        name='user-add-code'
    )
]
