from http import HTTPStatus
from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from accounts.forms import UserUpdateForm, ProfileUpdateForm


User = get_user_model()

class UpdateProfileTest(TestCase):

    def setUp(self) -> None:
        self.url = reverse("update_user_profile")
        self.template_name = "accounts/updateprofile.html"
        self.username = "testuser"
        self.email = "testuser@app.com"
        self.password = "testpassword"
        User.objects.create_user(
            username = self.username,
            email = self.email,
            password = self.password
        )

    def test_profile_update_page_exists(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, self.template_name)
        profile_form = response.context.get("profile_form", None)
        user_form = response.context.get("user_form", None)
        self.assertIsInstance(profile_form, ProfileUpdateForm)
        self.assertIsInstance(user_form, UserUpdateForm)
    
    def test_profile_and_user_update_forms_update_users(self):
        #self.client.login(username=self.username, password=self.password)
        request = HttpRequest()
        request.user = User.objects.get(id=1)
        request.POST = {
            "bio": "Sample bio text",
            "address": "123 django avenue",
            "first_name": "Updated",
            "last_name": "User",
            "username": "testuser"
        }
        profile_form = ProfileUpdateForm(instance=request.user.profile, data={
            "bio": request.POST.get("bio", None),
            "address": request.POST.get("address", None)
        })
        user_form = UserUpdateForm(instance=request.user, data={
            "first_name": request.POST.get("first_name", None),
            "last_name": request.POST.get("last_name", None),
            "username": request.POST.get("username", None)
        })
        self.assertTrue(profile_form.is_valid())
        self.assertTrue(user_form.is_valid())
        profile_form.save()
        user_form.save()
        self.assertEqual(request.user.username, request.POST.get("username", None))
        self.assertEqual(request.user.profile.bio, request.POST.get("bio", None))
