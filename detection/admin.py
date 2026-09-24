from django.contrib import admin
from .models import DetectionHistory


@admin.register(DetectionHistory)
class DetectionHistoryAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "detection_type",
        "predicted_class",
        "confidence",
        "model_name",
        "created_at",
    )

    list_filter = (
        "detection_type",
        "model_name",
        "created_at",
    )

    search_fields = (
        "predicted_class",
        "model_name",
        "user__username",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "created_at",
    )