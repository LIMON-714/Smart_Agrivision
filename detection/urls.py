from django.urls import path

from . import views


app_name = "detection"


urlpatterns = [


    path("",views.detection_home,name="detection",),
    path("image/",views.image_detection,name="image_detection",),
    path("video/",views.video_detection,name="video_detection",),
    path("camera/",views.camera_detection,name="camera_detection",),
    path("history/",views.history,name="detection_history",),
    path("history/<int:pk>/",views.detection_detail,name="detection_detail",),
    path("history/<int:pk>/delete/",views.delete_detection,name="delete_detection",),
]