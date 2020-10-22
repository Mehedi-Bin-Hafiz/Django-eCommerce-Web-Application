from django import forms
from django.contrib.auth import get_user_model

User=get_user_model()
class ContactForm(forms.Form):
    fullname = forms.CharField(widget = forms.TextInput(
        attrs={
            "class": "form-control","placeholder":"enter fullname", "id": "form_full_name",
        })
    )

    #here fullname act as name in html
    email = forms.EmailField(widget = forms.EmailInput(
        attrs={
            "class": "form-control","placeholder":"enter email", "id": "form_full_email",
        }))

    content = forms.CharField(widget = forms.Textarea(
        attrs={
            "class": "form-control","placeholder":"enter content", "id": "form_full_content",
        }))

class LoginForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(
        attrs={
            "class": "form-control","placeholder":"enter fullname", "id": "form_full_name",
        })
    )
    password =forms.CharField(widget = forms.PasswordInput(
        attrs={
            "class": "form-control","placeholder":"enter fullname", "id": "form_full_name",
        }))

class RegisterForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(
        attrs={
            "class": "form-control","placeholder":"enter fullname", "id": "form_full_name",
        })
    )

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "class": "form-control", "placeholder": "enter email", "id": "form_full_email",
        }))

    password = forms.CharField(widget = forms.PasswordInput(
        attrs={
            "class": "form-control","placeholder":"enter fullname", "id": "form_full_name",
        }))

    Confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": "form-control", "placeholder": "enter fullname", "id": "form_full_name",
        }))

    ## this part is confusing
    def clean(self):
        data = self.cleaned_data
        pass1 = data.get('password')
        pass2 = data.get('Confirm_password')
        if pass1 != pass2:
            raise forms.ValidationError("Password must match")
        else:
            return data

    ## this part is confusing

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is already taken.")
        else:
            return username
    def clean_email(self):
        email = self.cleaned_data.get('email')
        em = User.objects.filter(email=email)
        if em.exists():
            raise forms.ValidationError("Email is already taken")




