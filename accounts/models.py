from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    # =========================================================
    # CHOICES
    # =========================================================

    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )

    LANGUAGE_CHOICES = (
        ("English", "English"),
        ("Bangla", "Bangla"),
    )

    THEME_CHOICES = (
        ("Light", "Light"),
        ("Dark", "Dark"),
        ("System", "System"),
    )

    # =========================================================
    # USER
    # =========================================================

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
    )

    # =========================================================
    # PROFILE IMAGES
    # =========================================================

    profile_image = models.ImageField(
        upload_to="profile_images/",
        default="profile_images/default.png",
        blank=True,
        null=True,
    )

    cover_image = models.ImageField(
        upload_to="cover_images/",
        default="cover_images/default_cover.jpg",
        blank=True,
        null=True,
    )

    # =========================================================
    # PERSONAL INFORMATION
    # =========================================================

    phone = models.CharField(
        max_length=20,
        blank=True,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        blank=True,
    )

    # =========================================================
    # ADDRESS INFORMATION
    # =========================================================

    country = models.CharField(
        max_length=100,
        blank=True,
    )

    division = models.CharField(
        max_length=100,
        blank=True,
    )

    district = models.CharField(
        max_length=100,
        blank=True,
    )

    postal_code = models.CharField(
        max_length=20,
        blank=True,
    )

    address = models.TextField(
        blank=True,
    )

    # =========================================================
    # PROFESSIONAL INFORMATION
    # =========================================================

    profession = models.CharField(
        max_length=150,
        blank=True,
    )

    organization = models.CharField(
        max_length=150,
        blank=True,
    )

    website = models.URLField(
        blank=True,
    )

    bio = models.TextField(
        blank=True,
    )

    skills = models.TextField(
        blank=True,
        help_text="Separate skills with commas.",
    )

    # =========================================================
    # SOCIAL MEDIA LINKS
    # =========================================================

    facebook = models.URLField(
        blank=True,
    )

    linkedin = models.URLField(
        blank=True,
    )

    github = models.URLField(
        blank=True,
    )

    twitter = models.URLField(
        blank=True,
    )

    instagram = models.URLField(
        blank=True,
    )

    portfolio = models.URLField(
        blank=True,
    )

    # =========================================================
    # USER PREFERENCES
    # =========================================================

    language = models.CharField(
        max_length=20,
        choices=LANGUAGE_CHOICES,
        default="English",
    )

    theme = models.CharField(
        max_length=20,
        choices=THEME_CHOICES,
        default="System",
    )

    # =========================================================
    # NOTIFICATION SETTINGS
    # =========================================================

    email_notifications = models.BooleanField(
        default=True,
    )

    sms_notifications = models.BooleanField(
        default=False,
    )

    ai_alerts = models.BooleanField(
        default=True,
    )

    weekly_reports = models.BooleanField(
        default=True,
    )

    public_profile = models.BooleanField(
        default=True,
    )

    # =========================================================
    # TIMESTAMPS
    # =========================================================

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    # =========================================================
    # META
    # =========================================================

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        ordering = ["-created_at"]

    # =========================================================
    # STRING REPRESENTATION
    # =========================================================

    def __str__(self):
        return self.user.username