from django.urls import path, include
from .views import RegisterAPIView, LoginAPIView, UserAPIView, RefreshAPIView
urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("user/", UserAPIView.as_view(), name="user"),
    path("refresh/", RefreshAPIView.as_view(), name="refresh"),

]
