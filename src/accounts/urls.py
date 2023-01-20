from django.urls import path
from .views import register_user, login_page, logout_user


urlpatterns = [
    path("signup/", register_user, name="signup_page"),
    path("login/", login_page, name="login_page"),
    path("logout/", logout_user, name="logout"),
]
