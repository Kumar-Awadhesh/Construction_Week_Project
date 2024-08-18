from django.urls import path
from . import views

urlpatterns = [
    path("sign_up/", views.sign_up, name="sign_up"),
    path("login/", views.Login, name="login"),
    path("logout/", views.log_out, name="logout"),
]