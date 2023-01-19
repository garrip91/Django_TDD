from django.urls import path
from .views import register_user, login_page


urlpatterns = [
    path("signup/", register_user, name="signup_page"),
    path("login/", login_page, name="login_page"),
]
