from django import forms

from .models import User


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email", "phone_number", "national_id")
    
    def clean_email(self):
        email = str(self.cleaned_data["email"])

        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("This email is already exist!")
        return email
    
    def clean_username(self):
        username = str(self.cleaned_data["username"])

        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("This username is already exist!")
        return username
    


class UserRegisterForm(UserUpdateForm):
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ("username", "email", "password", "phone_number", "national_id", "confirm_password")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if not password or not confirm_password:
            raise forms.ValidationError('Enter the both of password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Password must match')
        return cleaned_data
    

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)