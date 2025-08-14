from django import forms
import re


class Login_Form(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={'class': 'email ele', 'placeholder': 'Enter your username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'password ele', 'placeholder': 'Password'}),
        required=True,
        validators=[
            lambda value: re.fullmatch(r'^(?=.*[A-Z])(?=.*\d)[A-Za-z\d@$!%*?&]{8,}$', value) or forms.ValidationError(
                "Password must be at least 8 characters long, include one uppercase letter and one number."
            )
        ]
    )


GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
]


class SignUp_Form(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "name ele", "placeholder": "Enter your name"}),
        max_length=150,
        required=True
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={"class": "email ele", "placeholder": "youremail@example.com"}),
        max_length=150,
        required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "password ele", "placeholder": "Password"}),
        required=True,
        validators=[
            lambda value: re.fullmatch(r'^(?=.*[A-Z])(?=.*\d)[A-Za-z\d@$!%*?&]{8,}$', value) or forms.ValidationError(
                "Password must be at least 8 characters long, include one uppercase letter and one number."
            )
        ]
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "password ele", "placeholder": "Confirm password"}),
        required=True,
        validators=[
            lambda value: re.fullmatch(r'^(?=.*[A-Z])(?=.*\d)[A-Za-z\d@$!%*?&]{8,}$', value) or forms.ValidationError(
                "Password must be at least 8 characters long, include one uppercase letter and one number."
            )
        ]
    )
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={"class": "dob ele", "type": "date"}),
        required=True
    )
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect(attrs={"class": "gender-container ele"}),
        label="Gender"
    )

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data.get("confirm_password")
        password = self.cleaned_data.get("password")

        if not confirm_password:
            raise forms.ValidationError("Confirm Password is required.")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return confirm_password


TYPE_CHOICES = [("0", "Suits"), ("1", "T-Shirts")]


class New_Product(forms.Form):
    product_name = forms.CharField(max_length=200, required=True)
    price = forms.DecimalField(required=True, decimal_places=2)
    quantity = forms.DecimalField(
        max_digits=10, required=True, decimal_places=2)
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}))
    photo = forms.CharField(max_length=100)
    rating = forms.DecimalField(decimal_places=2)
    product_type = forms.ChoiceField(choices=TYPE_CHOICES, required=True)

