from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "phone",
        "country",
        "profession",
        "organization",
        "public_profile",
        "created_at",
    )

    list_filter = (
        "gender",
        "country",
        "language",
        "theme",
        "public_profile",
        "email_notifications",
        "created_at",
    )

    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
        "user__email",
        "phone",
        "country",
        "profession",
        "organization",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (

        ("User Information", {
            "fields": (
                "user",
                "profile_image",
                "cover_image",
            )
        }),

        ("Personal Information", {
            "fields": (
                "phone",
                "date_of_birth",
                "gender",
            )
        }),

        ("Address", {
            "fields": (
                "country",
                "division",
                "district",
                "postal_code",
                "address",
            )
        }),

        ("Professional Information", {
            "fields": (
                "profession",
                "organization",
                "website",
                "bio",
                "skills",
            )
        }),

        ("Social Links", {
            "fields": (
                "facebook",
                "linkedin",
                "github",
                "twitter",
                "instagram",
                "portfolio",
            )
        }),

        ("Preferences", {
            "fields": (
                "language",
                "theme",
            )
        }),

        ("Notifications", {
            "fields": (
                "email_notifications",
                "sms_notifications",
                "ai_alerts",
                "weekly_reports",
                "public_profile",
            )
        }),

        ("System Information", {
            "fields": (
                "created_at",
                "updated_at",
            )
        }),

    )