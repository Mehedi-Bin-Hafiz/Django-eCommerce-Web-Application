from django import forms

class ContactForm(forms.Form):
    fullname = forms.CharField(widget = forms.TextInput(
        attrs={
            "class": "form-control","placeholder":"enter fullname", "id": "form_full_name", "name":"name"
        })
    )

    #here fullname act as name in html
    email = forms.EmailField(widget = forms.EmailInput(
        attrs={
            "class": "form-control","placeholder":"enter email", "id": "form_full_email","name":"email"
        }))
    content = forms.CharField(widget = forms.Textarea(
        attrs={
            "class": "form-control","placeholder":"enter content", "id": "form_full_content", "name":"content"
        }))

class LoginForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(
        attrs={
            "class": "form-control","placeholder":"enter fullname", "id": "form_full_name", "name":"name"
        })
    )
    password =forms.CharField(widget = forms.PasswordInput(
        attrs={
            "class": "form-control","placeholder":"enter fullname", "id": "form_full_name", "name":"name"
        }))