from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_user, login_page, logout_user, current_user_profile, update_user_profile


urlpatterns = [
    path("signup/", register_user, name="signup_page"),
    path("login/", login_page, name="login_page"),
    path("logout/", logout_user, name="logout"),
    
    path("password_reset/", auth_views.PasswordResetView.as_view(
        template_name = "accounts/password_reset.html"
    ), name="password_reset"),
    path("password_reset_done/", auth_views.PasswordResetDoneView.as_view(
        template_name = "accounts/password_reset_done.html"
    ), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name = "accounts/password_reset_confirm.html"
    ), name="password_reset_confirm"),
    path("password_reset_complete/", auth_views.PasswordResetCompleteView.as_view(
        template_name = "accounts/password_reset_complete.html"
    ), name="password_reset_complete"),
    path("current_user_profile/", current_user_profile, name="current_user_profile"),
    path("update_user_profile/", update_user_profile, name="update_user_profile"),
]
