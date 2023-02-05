from django.urls import path
from .views import index, post_detail, create_post


urlpatterns = [
    path("", index, name="homepage"),
    path("post/<int:id>/", post_detail, name="post_detail"),
    path("create_post/", create_post, name="create_post"),
]
