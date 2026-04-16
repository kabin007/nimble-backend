from django.urls import path
from .views import AuthViewSet

urlpatterns = [
    path("login/", AuthViewSet.as_view({"post": "login"}), name="login"),
    path("register/", AuthViewSet.as_view({"post": "register"}), name="register"),
    path("me/", AuthViewSet.as_view({"get": "me"}), name="current_user"),
]
