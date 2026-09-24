from pathlib import Path
import time

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .models import DetectionHistory
from .utils import get_yolo_model, predict_image




@login_required
def detection_home(request):

    detections = (
        DetectionHistory.objects
        .filter(user=request.user)
        .order_by("-created_at")
    )

    image_count = detections.filter(
        detection_type="image"
    ).count()

    video_count = detections.filter(
        detection_type="video"
    ).count()

    camera_count = detections.filter(
        detection_type="camera"
    ).count()

    context = {
        "detections": detections,

        "detection_count": detections.count(),

        "image_count": image_count,

        "video_count": video_count,

        "camera_count": camera_count,
    }

    return render(
        request,
        "detection/detection.html",
        context,
    )




@login_required
def image_detection(request):

    context = {
        "prediction": None,
        "confidence": None,
        "detection": None,
        "error": None,
        "model_name": "YOLO11 Classification",
        "confidence_status": None,
        "detection_date": None,
    }

    if request.method == "POST":

        uploaded_image = request.FILES.get("image")



        if uploaded_image is None:

            context["error"] = (
                "Please select an image first."
            )

            messages.error(
                request,
                context["error"],
            )

            return render(
                request,
                "detection/image_detection.html",
                context,
            )



        allowed_extensions = {
            ".jpg",
            ".jpeg",
            ".png",
            ".bmp",
            ".webp",
        }

        extension = Path(
            uploaded_image.name
        ).suffix.lower()

        if extension not in allowed_extensions:

            context["error"] = (
                "Invalid image format. "
                "Please upload JPG, JPEG, PNG, BMP or WEBP."
            )

            messages.error(
                request,
                context["error"],
            )

            return render(
                request,
                "detection/image_detection.html",
                context,
            )



        max_size = 10 * 1024 * 1024

        if uploaded_image.size > max_size:

            context["error"] = (
                "Image is too large. "
                "Maximum allowed size is 10 MB."
            )

            messages.error(
                request,
                context["error"],
            )

            return render(
                request,
                "detection/image_detection.html",
                context,
            )

        detection = None

        try:



            detection = DetectionHistory.objects.create(

                user=request.user,

                detection_type="image",

                image=uploaded_image,

                predicted_class="Processing...",

                confidence=0.0,

                model_name="YOLO11 Classification",
            )



            image_path = str(
                detection.image.path
            )



            predicted_class, confidence = predict_image(
                image_path
            )

            confidence = float(
                confidence
            )



            detection.predicted_class = (
                predicted_class
            )

            detection.confidence = (
                confidence
            )

            detection.model_name = (
                "YOLO11 Classification"
            )

            detection.save(
                update_fields=[
                    "predicted_class",
                    "confidence",
                    "model_name",
                ]
            )



            if confidence >= 80:

                confidence_status = (
                    "High Confidence"
                )

            elif confidence >= 50:

                confidence_status = (
                    "Medium Confidence"
                )

            else:

                confidence_status = (
                    "Low Confidence"
                )



            context.update({

                "prediction":
                    predicted_class,

                "confidence":
                    confidence,

                "detection":
                    detection,

                "confidence_status":
                    confidence_status,

                "model_name":
                    detection.model_name,

                "detection_date":
                    detection.created_at,

            })

            messages.success(
                request,
                "Image successfully analyzed.",
            )

        except Exception as error:

            context["error"] = str(
                error
            )

            messages.error(
                request,
                f"Image analysis failed: {error}",
            )



            if detection is not None:

                try:

                    if detection.image:

                        detection.image.delete(
                            save=False
                        )

                    detection.delete()

                except Exception:
                    pass

    return render(
        request,
        "detection/image_detection.html",
        context,
    )




@login_required
def video_detection(request):

    context = {
        "uploaded_video_url": None,
        "video_result": None,
        "error": None,
        "detection": None,
    }

    if request.method == "POST":

        uploaded_video = request.FILES.get(
            "video"
        )



        if not uploaded_video:

            context["error"] = (
                "Please select a video file first."
            )

            messages.error(
                request,
                context["error"],
            )

            return render(
                request,
                "detection/video_detection.html",
                context,
            )



        allowed_extensions = {
            ".mp4",
            ".avi",
            ".mov",
            ".mkv",
            ".webm",
        }

        extension = Path(
            uploaded_video.name
        ).suffix.lower()

        if extension not in allowed_extensions:

            context["error"] = (
                "Invalid video format. "
                "Please upload MP4, AVI, MOV, MKV or WEBM."
            )

            messages.error(
                request,
                context["error"],
            )

            return render(
                request,
                "detection/video_detection.html",
                context,
            )



        max_size = 100 * 1024 * 1024

        if uploaded_video.size > max_size:

            context["error"] = (
                "Video is too large. "
                "Maximum allowed size is 100 MB."
            )

            messages.error(
                request,
                context["error"],
            )

            return render(
                request,
                "detection/video_detection.html",
                context,
            )

        detection = None

        try:



            detection = DetectionHistory.objects.create(

                user=request.user,

                detection_type="video",

                video=uploaded_video,

                predicted_class="Processing...",

                confidence=0.0,

                model_name="YOLO11 Classification",
            )


            video_path = str(
                detection.video.path
            )



            context["uploaded_video_url"] = (
                detection.video.url
            )



            start_time = time.time()



            model = get_yolo_model()



            results = model.predict(
                source=video_path,
                verbose=False,
            )

            if not results:

                raise RuntimeError(
                    "YOLO did not return any prediction."
                )



            predictions = []

            for result in results:

                if result.probs is None:
                    continue

                class_index = int(
                    result.probs.top1
                )

                confidence = (
                    float(
                        result.probs.top1conf
                    )
                    * 100.0
                )

                names = result.names

                if isinstance(
                    names,
                    dict
                ):

                    predicted_class = names.get(
                        class_index,
                        str(class_index),
                    )

                else:

                    predicted_class = str(
                        names[class_index]
                    )

                predictions.append({

                    "class":
                        predicted_class,

                    "confidence":
                        confidence,
                })



            if not predictions:

                raise RuntimeError(
                    "No classification result was found."
                )



            best_prediction = max(
                predictions,
                key=lambda item:
                    item["confidence"],
            )

            predicted_class = (
                best_prediction["class"]
            )

            confidence = round(
                best_prediction["confidence"],
                2,
            )



            processing_time = round(
                time.time() - start_time,
                2,
            )


            if confidence >= 80:

                status = "high_confidence"

            elif confidence >= 50:

                status = "medium_confidence"

            else:

                status = "low_confidence"

            # ------------------------------------------------
            # SAVE RESULT TO DATABASE
            # ------------------------------------------------

            detection.predicted_class = (
                predicted_class
            )

            detection.confidence = (
                confidence
            )

            detection.model_name = (
                "YOLO11 Classification"
            )

            detection.save(
                update_fields=[
                    "predicted_class",
                    "confidence",
                    "model_name",
                ]
            )



            context["video_result"] = {

                "prediction":
                    predicted_class,

                "confidence":
                    confidence,

                "status":
                    status,

                "frames_analyzed":
                    len(predictions),

                "processing_time":
                    f"{processing_time} seconds",

                "model":
                    detection.model_name,

                "detection_date":
                    detection.created_at,
            }

            context["detection"] = (
                detection
            )

            messages.success(
                request,
                "Video successfully analyzed.",
            )

        except Exception as error:

            context["error"] = str(
                error
            )

            messages.error(
                request,
                f"Video analysis failed: {error}",
            )



            if detection is not None:

                try:

                    if detection.video:

                        detection.video.delete(
                            save=False
                        )

                    if detection.result_video:

                        detection.result_video.delete(
                            save=False
                        )

                    detection.delete()

                except Exception:
                    pass

    return render(
        request,
        "detection/video_detection.html",
        context,
    )




@login_required
def camera_detection(request):

    context = {

        "prediction": None,

        "confidence": None,

        "error": None,

        "model_name":
            "YOLO11 Classification",

        "detection_date": None,

        "detection": None,

        "confidence_status": None,
    }

    if request.method == "POST":

        uploaded_image = request.FILES.get(
            "image"
        )



        if uploaded_image is None:

            context["error"] = (
                "No captured camera image was received. "
                "Please capture an image first."
            )

            messages.error(
                request,
                context["error"],
            )

            return render(
                request,
                "detection/camera_detection.html",
                context,
            )



        allowed_extensions = {
            ".jpg",
            ".jpeg",
            ".png",
            ".webp",
            ".bmp",
        }

        extension = Path(
            uploaded_image.name
        ).suffix.lower()

        if extension not in allowed_extensions:

            context["error"] = (
                "Invalid camera image format."
            )

            messages.error(
                request,
                context["error"],
            )

            return render(
                request,
                "detection/camera_detection.html",
                context,
            )



        max_size = 10 * 1024 * 1024

        if uploaded_image.size > max_size:

            context["error"] = (
                "Captured image is too large. "
                "Maximum allowed size is 10 MB."
            )

            messages.error(
                request,
                context["error"],
            )

            return render(
                request,
                "detection/camera_detection.html",
                context,
            )

        detection = None

        try:



            detection = DetectionHistory.objects.create(

                user=request.user,

                detection_type="camera",

                image=uploaded_image,

                predicted_class="Processing...",

                confidence=0.0,

                model_name="YOLO11 Classification",
            )



            image_path = str(
                detection.image.path
            )



            predicted_class, confidence = predict_image(
                image_path
            )

            confidence = float(
                confidence
            )



            detection.predicted_class = (
                predicted_class
            )

            detection.confidence = (
                confidence
            )

            detection.model_name = (
                "YOLO11 Classification"
            )

            detection.save(
                update_fields=[
                    "predicted_class",
                    "confidence",
                    "model_name",
                ]
            )



            if confidence >= 80:

                confidence_status = (
                    "High Confidence"
                )

            elif confidence >= 50:

                confidence_status = (
                    "Medium Confidence"
                )

            else:

                confidence_status = (
                    "Low Confidence"
                )



            context.update({

                "prediction":
                    predicted_class,

                "confidence":
                    confidence,

                "detection":
                    detection,

                "model_name":
                    detection.model_name,

                "confidence_status":
                    confidence_status,

                "detection_date":
                    detection.created_at,
            })

            messages.success(
                request,
                "Camera image successfully analyzed.",
            )

        except Exception as error:

            context["error"] = str(
                error
            )

            messages.error(
                request,
                f"Camera analysis failed: {error}",
            )



            if detection is not None:

                try:

                    if detection.image:

                        detection.image.delete(
                            save=False
                        )

                    detection.delete()

                except Exception:
                    pass

    return render(
        request,
        "detection/camera_detection.html",
        context,
    )



@login_required
def history(request):

    detections = (
        DetectionHistory.objects
        .filter(
            user=request.user
        )
        .order_by("-created_at")
    )



    image_count = detections.filter(
        detection_type="image"
    ).count()

    video_count = detections.filter(
        detection_type="video"
    ).count()

    camera_count = detections.filter(
        detection_type="camera"
    ).count()

    context = {

        "detections":
            detections,

        "detection_count":
            detections.count(),

        "image_count":
            image_count,

        "video_count":
            video_count,

        "camera_count":
            camera_count,
    }

    return render(
        request,
        "detection/history.html",
        context,
    )




@login_required
def detection_detail(request, pk):

    detection = get_object_or_404(

        DetectionHistory,

        pk=pk,

        user=request.user,
    )

    return render(

        request,

        "detection/detection_detail.html",

        {
            "detection":
                detection,
        },
    )



@login_required
def delete_detection(request, pk):

    detection = get_object_or_404(

        DetectionHistory,

        pk=pk,

        user=request.user,
    )

    if request.method == "POST":

        

        if detection.image:

            try:

                detection.image.delete(
                    save=False
                )

            except Exception:
                pass


        if detection.video:

            try:

                detection.video.delete(
                    save=False
                )

            except Exception:
                pass


        if detection.result_video:

            try:

                detection.result_video.delete(
                    save=False
                )

            except Exception:
                pass



        detection.delete()

        messages.success(
            request,
            "Detection history item deleted successfully.",
        )

        return redirect(
            "detection:detection_history"
        )

    return render(

        request,

        "detection/delete_detection.html",

        {
            "detection":
                detection,
        },
    )