from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth.decorators import login_required

class SignUpForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=10, validators=[MinLengthValidator(10)], required=True)
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ["full_name", "phone", "email", "username"]
