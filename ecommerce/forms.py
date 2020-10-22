from django import forms

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

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": "form-control", "placeholder": "enter fullname", "id": "form_full_name",
        }))

    def clean(self):
        data = self.cleaned_data

        pass1 = data.get('password')
        pass2 = data.get('password2')

        if pass1 != pass2:
            raise forms.ValidationError("Password must match")
        else:
            return data

