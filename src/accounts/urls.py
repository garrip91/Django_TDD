from django.urls import path
from .views import register_user


urlpatterns = [
    path("signup/", register_user, name="signup_page"),
]
