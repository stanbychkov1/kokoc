from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import CharField, PasswordInput, TextInput, EmailField, \
    ModelForm

User = get_user_model()


class UserAuthForm(AuthenticationForm):
    username = EmailField(label='E-mail',
                             widget=TextInput(attrs={'autofocus': True}))
    password = CharField(
        label='Пароль',
        strip=False,
        widget=PasswordInput(attrs={'autocomplete': 'current-password'}),
    )


class UserRegistrationForm(UserCreationForm):
    password1 = CharField(
        label='Пароль',
        strip=False,
        widget=PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = None

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')
        labels = {
            'username': 'Пользователь',
        }


class UserForm(ModelForm):

    def __init__(self, disable_fields=False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['balance'].disabled = True
        self.fields['background_color'].disabled = True
        self.fields['username_color'].disabled = True
        self.fields['passed_test_quantity'].disabled = True
        if disable_fields:
            for field in self.fields:
                self.fields[field].disabled = True

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username', 'email', 'balance',
                  'background_color', 'username_color', 'passed_test_quantity')

