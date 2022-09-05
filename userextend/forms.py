from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm, \
    SetPasswordForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select, DateInput

from userextend.models import UserExtend


class SelectInput:
    pass


class UserExtendForm(UserCreationForm):
    class Meta:
        model = UserExtend
        fields = ['first_name', 'last_name', 'email', 'email_confirmation', 'username', 'phone_number']

        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'Please enter your first name :', 'class': 'form-control'}),
            'last_name': TextInput(attrs={'placeholder': 'Please enter your last name : ', 'class': 'form-control'}),
            'email': EmailInput(attrs={'placeholder': 'Please enter your email :', 'class': 'form-control'}),
            'username': TextInput(attrs={'placeholder': 'Please enter your username :', 'class': 'form-control'}),
            'email_confirmation': EmailInput(
                attrs={'placeholder': 'Please confirm your email :', 'class': 'form-control'}),
            'phone_number': TextInput(
                attrs={'placeholder': 'Please enter your phone number : ', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(UserExtendForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Please enter your password'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Please enter your password'








class AuthenticationLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your username'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your password'})


class PasswordChangeFormExtend(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter old password'})
        self.fields['new_password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter new password'})
        self.fields['new_password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please conform new password'})


class PasswordResetFormExtend(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter e-mail adress'})


class SetPasswordFormExtend(SetPasswordForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter a new password'})
        self.fields['new_password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please confirm your new password'})
