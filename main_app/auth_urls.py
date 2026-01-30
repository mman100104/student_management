"""Authentication URLs"""
from django.urls import path
from .views import login_page, get_attendance, showFirebaseJS, doLogin, logout_user

urlpatterns = [
    path("", login_page, name='login_page'),
    path("get_attendance", get_attendance, name='get_attendance'),
    path("firebase-messaging-sw.js", showFirebaseJS, name='showFirebaseJS'),
    path("doLogin/", doLogin, name='user_login'),
    path("logout_user/", logout_user, name='user_logout'),
]