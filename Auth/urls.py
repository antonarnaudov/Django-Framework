from django.urls import path

from Auth.views import register_user, login_user, logout_user, view_user_profile, edit_user_profile

urlpatterns = [
    path('register/', register_user, name='register user'),
    path('login/', login_user, name='login user'),
    path('logout/', logout_user, name='logout user'),

    path('view/userprofile/<int:pk>/', view_user_profile, name='view profile'),
    path('edit/userprofile/<int:pk>/', edit_user_profile, name='edit profile'),
]
