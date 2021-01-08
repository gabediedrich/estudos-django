from django import forms
from django.contrib.auth.models import User
from django.db.models.functions import datetime
from django.utils.translation import ugettext_lazy as _

import re

from usuarios.models import UserInfo

class UserSignUpForm(forms.ModelForm):
    """
    Um formulário que cria um usuário, com privilégios limitados
    """
    password1 = forms.CharField(label=_("Senha"),
                                widget=forms.PasswordInput,
                                help_text=_("Digite a mesma senha em ambos os campos."))
    password2 = forms.CharField(label=_("Confirme a senha"),
                                widget=forms.PasswordInput,
                                help_text=_("Digite a mesma senha em ambos os campos."))

    class Meta:
        model = UserInfo
        fields = ["first_name", "last_name", "email", "username", 
                  "phone_number", "description"]


    def clean_password(self):
        """
        :return: retorna a senha correta
        """
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise self.ValidationError(_("As senhas digitadas não conferem"))
        if not self.validate_password_strength():
            raise self.ValidationError(_('A senha deve conter ao menos um número'))

        return password2

    def clean_phone_number(self):
        """
        Checa se o telefone é válido
        :return: retorna o telefone
        """
        phone_number = self.cleaned_data['phone_number']
        if not re.match(r'\(?([1-9]{2,3})\)?([0-9]{9})', phone_number):
            raise forms.ValidationError(_("Insira um número de telefone nacional válido"), code= 'invalid_phone')
    
        return phone_number

    def clean_username(self):
        """
        check username already exists
        :return: cleaned username
        """
        username = self.cleaned_data.get('username', None)
        if User.objects.filter(username__iexact=username):
            raise forms.ValidationError(_('That username is already in use, please use a new one!'))
        return username

    def clean_email(self):
        """
        check email already exists
        :return: cleaned email
        """
        email = self.cleaned_data.get('email', None)
        if User.objects.filter(email__iexact=email):
            raise forms.ValidationError(_('That email is already in registered, please login using the login button!'))
        return email

    def validate_password_strength(self):
        """Validates that a password is as least 7 characters long and has at least
        1 digit and 1 letter.
        """
        min_length = 8
        value = self.cleaned_data['password1']

        if len(value) < min_length:
            raise forms.ValidationError(_('Password must be at least {0} characters long.').format(min_length))

        # check for digit
        if not any(char.isdigit() for char in value):
            raise forms.ValidationError(_('Password must contain at least 1 digit.'))

        # check for letter
        if not any(char.isalpha() for char in value):
            raise forms.ValidationError(_('Password must contain at least 1 letter.'))

        return True

    def save(self, commit=True):
        """
        Add password and save user
        :param commit: save the user by default
        :return: The saved user
        """
        user = super(UserSignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = False
        if commit:
            user.save()
        return user
