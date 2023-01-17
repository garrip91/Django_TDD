from django.urls import path
from .views import index, post_detail


urlpatterns = [
    path("", index, name="homepage"),
    path("post/<int:id>/", post_detail, name="post_detail")
]
