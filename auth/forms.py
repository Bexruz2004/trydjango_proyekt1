from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class MyUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': "form-control",
            "placeholder": "Username",
            'name': 'username'
        })

        self.fields['password1'].widget.attrs.update({
            'class': "form-control",
            "name": "password1",
            "type": "password",
            "autocomplete": "off",
            "id": "password1",
            "placeholder": "password"
            })

        self.fields['password2'].widget.attrs.update({
            'class': "form-control",
            "name": "password2",
            "type": "password",
            "autocomplete": "off",
            "id": "password2",
            "placeholder": "confirm password"
        })


class MyAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(MyAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': "form-control",
            "placeholder": "Username",
            'name': 'username'
        })

        self.fields['password'].widget.attrs.update({
            'class': "form-control",
            "name": "password",
            "type": "password",
            "autocomplete": "off",
            "id": "password",
            "placeholder": "password"
            })
