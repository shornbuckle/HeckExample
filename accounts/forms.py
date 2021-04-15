from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserRegisterData, User


class ClientUserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].label = "Username"
        self.fields["email"].label = "Email Address"
        self.fields["first_name"].label = "First Name"
        self.fields["last_name"].label = "Last Name"
        self.fields["about"].label = "Your Bio"

    l_choices = (("ny", "New York"), ("ca", "California"))
    ny_choices = (
        ("Manhattan", "Manhattan"),
        ("Brooklyn", "Brooklyn"),
        ("Queens", "Queens"),
        ("Staten Island", "Staten Island"),
        ("Bronx", "Bronx"),
    )

    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    city = forms.ChoiceField(choices=ny_choices)
    state = forms.ChoiceField(choices=l_choices)
    zip_code = forms.CharField(required=True)
    about = forms.CharField(required=False)


    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
            "email",
            "first_name",
            "last_name",
            "address",
            "city",
            "state",
            "zip_code",
            "about",
        ]
        help_texts = {
            "username": ("Username can contain Letters, digits and @/./+/-/_ only.")
        }


class ClientUpdateForm(forms.ModelForm):
    class Meta:
        model = UserRegisterData
        fields = ["user_profile_image"]
        labels = {"user_profile_image": ("User Profile Picture")}


class ClientUserUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["about"].label = "Your Bio"
        self.fields["username"].label = "Username"
        self.fields["first_name"].label = "First Name"
        self.fields["last_name"].label = "Last Name"

    l_choices = (("ny", "New York"), ("ca", "California"))
    ny_choices = (
        ("Manhattan", "Manhattan"),
        ("Brooklyn", "Brooklyn"),
        ("Queens", "Queens"),
        ("Staten Island", "Staten Island"),
        ("Bronx", "Bronx"),
    )

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    city = forms.ChoiceField(choices=ny_choices)
    state = forms.ChoiceField(choices=l_choices)
    zip_code = forms.CharField(required=True)
    about = forms.CharField(required=False)

    class Meta:
        model = User
        fields = [
            "about",
            "username",
            "first_name",
            "last_name",
            "address",
            "city",
            "state",
            "zip_code",
        ]
        help_texts = {
            "username": ("DONT UPDATE USERNAME")
        }

