from django import forms
from .models import PersonModel
from django.utils.translation import gettext_lazy as _


class PersonCreateModelForm(forms.ModelForm):
    class Meta:
        model = PersonModel
        fields = [
            "firstname",
            "lastName",
            "username",
            "password",
            "email",
        ]
        labels = {
            'firstname' : _("First Name"),
            "lastName" : _("Last Name"),
            "username" : _("Username"),
            "password" : _("Password"),
            "email" : _("Email")
        }
        widgets = {
            "password" : forms.PasswordInput(),            
        }

        
class PersonLoginForm(forms.Form):
    username = forms.CharField(max_length= 50,label="Kullanıcı Adı")
    password = forms.CharField(
        max_length=50,
        label="Parola",
        widget=forms.PasswordInput,
    )