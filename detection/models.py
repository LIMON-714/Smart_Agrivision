from django.conf import settings
from django.db import models


class DetectionHistory(models.Model):



    DETECTION_TYPE_CHOICES = [
        ("image", "Image"),
        ("video", "Video"),
        ("camera", "Live Camera"),
    ]

    detection_type = models.CharField(
        max_length=20,
        choices=DETECTION_TYPE_CHOICES,
        default="image",
    )




    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="detection_history",
    )



    image = models.ImageField(
        upload_to="detections/images/%Y/%m/%d/",
        blank=True,
        null=True,
    )



    video = models.FileField(
        upload_to="detections/videos/%Y/%m/%d/",
        blank=True,
        null=True,
    )



    result_video = models.FileField(
        upload_to="detections/results/%Y/%m/%d/",
        blank=True,
        null=True,
    )

   
    # PREDICTED CLASS
  

    predicted_class = models.CharField(
        max_length=255,
        default="Unknown",
    )


    # CONFIDENCE
  

    confidence = models.FloatField(
        default=0.0,
    )

    # MODEL NAME
    

    model_name = models.CharField(
        max_length=100,
        default="YOLO11 Classification",
    )

    
    # CREATED DATE
    

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    
    # META
    

    class Meta:
        ordering = ["-created_at"]

        verbose_name = "Detection History"

        verbose_name_plural = "Detection Histories"

    # DISPLAY HELPERS
   

    @property
    def type_label(self):
        """
        Human readable detection type.
        """

        return dict(
            self.DETECTION_TYPE_CHOICES
        ).get(
            self.detection_type,
            "Detection",
        )

    @property
    def confidence_status(self):
        """
        Confidence status calculated from real DB confidence.
        """

        if self.predicted_class == "Processing...":
            return "Processing"

        if self.confidence >= 80:
            return "High Confidence"

        if self.confidence >= 50:
            return "Medium Confidence"

        return "Low Confidence"

    @property
    def file_name(self):
        """
        Return the actual stored file name.
        """

        if self.detection_type == "video" and self.video:
            return self.video.name.split("/")[-1]

        if self.image:
            return self.image.name.split("/")[-1]

        return "No file"

   
    # STRING
    

    def __str__(self):
        return (
            f"{self.type_label} | "
            f"{self.predicted_class} | "
            f"{self.confidence:.2f}%"
        )