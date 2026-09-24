from pathlib import Path

from django.conf import settings
from ultralytics import YOLO



_model = None




YOLO_MODEL_PATH = (
    Path(settings.BASE_DIR)
    / "AI"
    / "notebooks"
    / "YOLO_Models"
    / "classification_runs"
    / "smartagrivision_yolo_classification_cpu"
    / "weights"
    / "best.pt"
)



def get_yolo_model():
    """
    Load the YOLO classification model once and cache it.
    """

    global _model

    # Return cached model
    if _model is not None:
        return _model

    # Check model file
    if not YOLO_MODEL_PATH.exists():
        raise FileNotFoundError(
            f"YOLO model not found:\n{YOLO_MODEL_PATH}"
        )

    try:
        _model = YOLO(
            str(YOLO_MODEL_PATH)
        )

    except Exception as error:
        raise RuntimeError(
            f"Failed to load YOLO model: {error}"
        ) from error

    return _model




def predict_image(image_path):
    """
    Run YOLO classification on one image.

    Returns:
        predicted_class: class name
        confidence_percentage: confidence in percentage
    """

    model = get_yolo_model()

    # Important for WindowsPath / Path objects
    image_path = str(image_path)

    results = model.predict(
        source=image_path,
        verbose=False
    )

    if not results:
        raise RuntimeError(
            "YOLO did not return any prediction."
        )

    result = results[0]

    # Classification model must have probs
    if result.probs is None:
        raise RuntimeError(
            "The loaded YOLO model is not a classification model."
        )

    # Top class index
    top_class_index = int(
        result.probs.top1
    )

    # Confidence
    confidence = float(
        result.probs.top1conf
    )

    # Class names
    names = result.names

    if isinstance(names, dict):

        predicted_class = names.get(
            top_class_index,
            str(top_class_index)
        )

    else:

        predicted_class = str(
            names[top_class_index]
        )

    # Convert to percentage
    confidence_percentage = (
        confidence * 100.0
    )

    return (
        predicted_class,
        confidence_percentage
    )