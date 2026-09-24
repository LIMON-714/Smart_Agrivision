from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm

from .models import Profile


# =========================================================
# REGISTER FORM
# =========================================================

class RegisterForm(UserCreationForm):

    first_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "First Name",
            }
        ),
    )

    last_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Last Name",
            }
        ),
    )

    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Username",
                "autocomplete": "username",
            }
        ),
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Email Address",
                "autocomplete": "email",
            }
        ),
    )

    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Password",
                "autocomplete": "new-password",
            }
        ),
    )

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirm Password",
                "autocomplete": "new-password",
            }
        ),
    )

    class Meta:

        model = User

        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        )

    # ---------------------------------------------------------
    # EMAIL VALIDATION
    # ---------------------------------------------------------

    def clean_email(self):

        email = self.cleaned_data.get("email")

        if not email:
            raise forms.ValidationError(
                "Email address is required."
            )

        email = email.strip().lower()

        if User.objects.filter(
            email__iexact=email
        ).exists():

            raise forms.ValidationError(
                "This email is already registered."
            )

        return email

    # ---------------------------------------------------------
    # USERNAME VALIDATION
    # ---------------------------------------------------------

    def clean_username(self):

        username = self.cleaned_data.get("username")

        if not username:
            raise forms.ValidationError(
                "Username is required."
            )

        username = username.strip()

        if User.objects.filter(
            username__iexact=username
        ).exists():

            raise forms.ValidationError(
                "This username is already taken."
            )

        return username

    # ---------------------------------------------------------
    # SAVE USER
    # ---------------------------------------------------------

    def save(self, commit=True):

        user = super().save(commit=False)

        user.first_name = self.cleaned_data[
            "first_name"
        ].strip()

        user.last_name = self.cleaned_data[
            "last_name"
        ].strip()

        user.username = self.cleaned_data[
            "username"
        ].strip()

        user.email = self.cleaned_data[
            "email"
        ].strip().lower()

        if commit:
            user.save()

        return user


# =========================================================
# USER UPDATE FORM
# =========================================================

class UserUpdateForm(forms.ModelForm):

    class Meta:

        model = User

        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
        ]

        widgets = {

            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "First Name",
                }
            ),

            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Last Name",
                }
            ),

            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Username",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email Address",
                }
            ),
        }

    # ---------------------------------------------------------
    # EMAIL VALIDATION
    # ---------------------------------------------------------

    def clean_email(self):

        email = self.cleaned_data.get("email")

        if not email:
            return ""

        email = email.strip().lower()

        queryset = User.objects.filter(
            email__iexact=email
        ).exclude(
            pk=self.instance.pk
        )

        if queryset.exists():

            raise forms.ValidationError(
                "This email is already used by another account."
            )

        return email

    # ---------------------------------------------------------
    # USERNAME VALIDATION
    # ---------------------------------------------------------

    def clean_username(self):

        username = self.cleaned_data.get("username")

        if not username:
            raise forms.ValidationError(
                "Username is required."
            )

        username = username.strip()

        queryset = User.objects.filter(
            username__iexact=username
        ).exclude(
            pk=self.instance.pk
        )

        if queryset.exists():

            raise forms.ValidationError(
                "This username is already taken."
            )

        return username


# =========================================================
# PROFILE UPDATE FORM
# =========================================================

class ProfileUpdateForm(forms.ModelForm):

    class Meta:

        model = Profile

        fields = [

            # Profile Images
            "profile_image",
            "cover_image",

            # Personal Information
            "phone",
            "date_of_birth",
            "gender",

            # Address
            "country",
            "division",
            "district",
            "postal_code",
            "address",

            # Professional
            "profession",
            "organization",
            "website",
            "bio",
            "skills",

            # Social Media
            "facebook",
            "linkedin",
            "github",
            "twitter",
            "instagram",
            "portfolio",

            # Preferences
            "language",
            "theme",

            # Notifications
            "email_notifications",
            "sms_notifications",
            "ai_alerts",
            "weekly_reports",
            "public_profile",
        ]

        widgets = {

            # -------------------------------------------------
            # IMAGES
            # -------------------------------------------------

            "profile_image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*",
                }
            ),

            "cover_image": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": "image/*",
                }
            ),

            # -------------------------------------------------
            # PERSONAL INFORMATION
            # -------------------------------------------------

            "phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Phone Number",
                }
            ),

            "date_of_birth": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "gender": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            # -------------------------------------------------
            # ADDRESS
            # -------------------------------------------------

            "country": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Country",
                }
            ),

            "division": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Division",
                }
            ),

            "district": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "District",
                }
            ),

            "postal_code": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Postal Code",
                }
            ),

            "address": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Full Address",
                }
            ),

            # -------------------------------------------------
            # PROFESSIONAL
            # -------------------------------------------------

            "profession": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Profession",
                }
            ),

            "organization": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Organization",
                }
            ),

            "website": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://example.com",
                }
            ),

            "bio": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Tell us about yourself...",
                }
            ),

            "skills": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Python, Django, AI, Machine Learning",
                }
            ),

            # -------------------------------------------------
            # SOCIAL MEDIA
            # -------------------------------------------------

            "facebook": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://facebook.com/username",
                }
            ),

            "linkedin": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://linkedin.com/in/username",
                }
            ),

            "github": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://github.com/username",
                }
            ),

            "twitter": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://twitter.com/username",
                }
            ),

            "instagram": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://instagram.com/username",
                }
            ),

            "portfolio": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://yourportfolio.com",
                }
            ),

            # -------------------------------------------------
            # PREFERENCES
            # -------------------------------------------------

            "language": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "theme": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            # -------------------------------------------------
            # NOTIFICATIONS
            # -------------------------------------------------

            "email_notifications": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),

            "sms_notifications": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),

            "ai_alerts": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),

            "weekly_reports": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),

            "public_profile": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }

    # ---------------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------------

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # Fields that are allowed to remain empty
        optional_fields = [

            "profile_image",
            "cover_image",

            "phone",
            "date_of_birth",
            "gender",

            "country",
            "division",
            "district",
            "postal_code",
            "address",

            "profession",
            "organization",
            "website",
            "bio",
            "skills",

            "facebook",
            "linkedin",
            "github",
            "twitter",
            "instagram",
            "portfolio",

            "language",
            "theme",

            "email_notifications",
            "sms_notifications",
            "ai_alerts",
            "weekly_reports",
            "public_profile",
        ]

        for field_name in optional_fields:

            if field_name in self.fields:

                self.fields[
                    field_name
                ].required = False


# =========================================================
# CHANGE PASSWORD FORM
# =========================================================

class CustomPasswordChangeForm(
    PasswordChangeForm
):

    def __init__(self, *args, **kwargs):

        super().__init__(
            *args,
            **kwargs
        )

        # -------------------------------------------------
        # OLD PASSWORD
        # -------------------------------------------------

        self.fields[
            "old_password"
        ].widget.attrs.update({

            "class": "form-control",
            "placeholder": "Current Password",
            "autocomplete": "current-password",
        })

        # -------------------------------------------------
        # NEW PASSWORD
        # -------------------------------------------------

        self.fields[
            "new_password1"
        ].widget.attrs.update({

            "class": "form-control",
            "placeholder": "New Password",
            "autocomplete": "new-password",
        })

        # -------------------------------------------------
        # CONFIRM PASSWORD
        # -------------------------------------------------

        self.fields[
            "new_password2"
        ].widget.attrs.update({

            "class": "form-control",
            "placeholder": "Confirm New Password",
            "autocomplete": "new-password",
        })