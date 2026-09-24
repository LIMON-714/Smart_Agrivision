/* ============================================================
   SmartAgriVision - Global JavaScript
   Camera + Video + Global Functions
   ============================================================ */

document.addEventListener("DOMContentLoaded", function () {

    "use strict";

    console.log(
        "SmartAgriVision script.js loaded successfully."
    );


    /* ============================================================
       CAMERA DETECTION
       ============================================================ */

    const cameraVideo =
        document.getElementById("cameraVideo");

    const cameraCanvas =
        document.getElementById("cameraCanvas");

    const cameraContainer =
        document.getElementById("cameraContainer");

    const cameraPlaceholder =
        document.getElementById("cameraPlaceholder");

    const cameraStatus =
        document.getElementById("cameraStatus");

    const startCameraButton =
        document.getElementById("startCameraButton");

    const captureImageButton =
        document.getElementById("captureImageButton");

    const stopCameraButton =
        document.getElementById("stopCameraButton");

    const capturedImageContainer =
        document.getElementById("capturedImageContainer");

    const capturedImage =
        document.getElementById("capturedImage");

    const cameraImageInput =
        document.getElementById("cameraImageInput");

    const analyzeImageButton =
        document.getElementById("analyzeImageButton");

    const cameraDetectionForm =
        document.getElementById("cameraDetectionForm");

    const cameraProcessingMessage =
        document.getElementById(
            "cameraProcessingMessage"
        );


    let cameraStream = null;


    /* ============================================================
       CAMERA STATUS
       ============================================================ */

    function updateCameraStatus(
        text,
        type = "secondary",
        icon = "fa-circle"
    ) {

        if (!cameraStatus) {
            return;
        }

        cameraStatus.className =
            "badge px-3 py-2";

        if (type === "success") {

            cameraStatus.classList.add(
                "bg-success"
            );

        } else if (type === "danger") {

            cameraStatus.classList.add(
                "bg-danger"
            );

        } else if (type === "warning") {

            cameraStatus.classList.add(
                "bg-warning",
                "text-dark"
            );

        } else {

            cameraStatus.classList.add(
                "bg-secondary"
            );
        }

        cameraStatus.innerHTML =
            `<i class="fa-solid ${icon} me-1"></i>${text}`;
    }


    /* ============================================================
       CAMERA SUPPORT CHECK
       ============================================================ */

    function cameraSupported() {

        return (
            navigator.mediaDevices &&
            typeof navigator.mediaDevices.getUserMedia ===
                "function"
        );
    }


    /* ============================================================
       START CAMERA
       ============================================================ */

    async function startCamera() {

        if (!cameraVideo) {
            console.warn(
                "cameraVideo element was not found."
            );
            return;
        }

        if (!cameraSupported()) {

            alert(
                "Camera access is not supported by this browser."
            );

            updateCameraStatus(
                "Camera Not Supported",
                "danger",
                "fa-circle-xmark"
            );

            return;
        }


        /* --------------------------------------------------------
           Stop previous stream if one exists
           -------------------------------------------------------- */

        if (cameraStream) {

            cameraStream
                .getTracks()
                .forEach(function (track) {
                    track.stop();
                });

            cameraStream = null;
        }


        try {

            /* ----------------------------------------------------
               Request camera
               ---------------------------------------------------- */

            cameraStream =
                await navigator.mediaDevices.getUserMedia({

                    video: {
                        facingMode: {
                            ideal: "environment"
                        },

                        width: {
                            ideal: 1280
                        },

                        height: {
                            ideal: 720
                        }
                    },

                    audio: false
                });


            /* ----------------------------------------------------
               Attach stream
               ---------------------------------------------------- */

            cameraVideo.srcObject =
                cameraStream;


            cameraVideo.style.display =
                "block";


            /* ----------------------------------------------------
               Make sure video has a fixed camera area
               ---------------------------------------------------- */

            cameraVideo.style.width =
                "100%";

            cameraVideo.style.height =
                "420px";

            cameraVideo.style.maxHeight =
                "420px";

            cameraVideo.style.objectFit =
                "cover";

            cameraVideo.style.backgroundColor =
                "#111";


            /* ----------------------------------------------------
               Hide placeholder
               ---------------------------------------------------- */

            if (cameraPlaceholder) {

                cameraPlaceholder.style.display =
                    "none";
            }


            /* ----------------------------------------------------
               Show camera container
               ---------------------------------------------------- */

            if (cameraContainer) {

                cameraContainer.style.minHeight =
                    "420px";

                cameraContainer.style.height =
                    "420px";
            }


            /* ----------------------------------------------------
               Wait for video metadata
               ---------------------------------------------------- */

            try {

                await cameraVideo.play();

            } catch (playError) {

                console.warn(
                    "Video autoplay/play warning:",
                    playError
                );
            }


            /* ----------------------------------------------------
               Buttons
               ---------------------------------------------------- */

            if (startCameraButton) {

                startCameraButton.disabled =
                    true;
            }


            if (captureImageButton) {

                captureImageButton.disabled =
                    false;
            }


            if (stopCameraButton) {

                stopCameraButton.disabled =
                    false;
            }


            /* ----------------------------------------------------
               Status
               ---------------------------------------------------- */

            updateCameraStatus(
                "Camera On",
                "success",
                "fa-video"
            );


            console.log(
                "Camera started successfully."
            );

        } catch (error) {

            console.error(
                "Camera access error:",
                error
            );

            cameraStream = null;


            let errorMessage =
                "Unable to access camera.";


            if (
                error.name ===
                "NotAllowedError"
            ) {

                errorMessage =
                    "Camera permission was denied. Please allow camera access in your browser.";

            } else if (
                error.name ===
                "NotFoundError"
            ) {

                errorMessage =
                    "No camera was found on this device.";

            } else if (
                error.name ===
                "NotReadableError"
            ) {

                errorMessage =
                    "Camera is already being used by another application.";

            } else if (
                error.name ===
                "OverconstrainedError"
            ) {

                errorMessage =
                    "The requested camera configuration is not available.";

            } else if (
                error.name ===
                "SecurityError"
            ) {

                errorMessage =
                    "Camera access is blocked by browser security settings.";

            } else if (
                error.name ===
                "AbortError"
            ) {

                errorMessage =
                    "Camera startup was interrupted.";
            }


            alert(errorMessage);


            updateCameraStatus(
                "Camera Error",
                "danger",
                "fa-circle-xmark"
            );
        }
    }


    /* ============================================================
       STOP CAMERA
       ============================================================ */

    function stopCamera(
        keepCapturedImage = true
    ) {

        if (cameraStream) {

            cameraStream
                .getTracks()
                .forEach(function (track) {

                    track.stop();

                });

            cameraStream = null;
        }


        if (cameraVideo) {

            cameraVideo.pause();

            cameraVideo.srcObject =
                null;

            cameraVideo.style.display =
                "none";
        }


        if (cameraContainer) {

            cameraContainer.style.height =
                "420px";

            cameraContainer.style.minHeight =
                "420px";
        }


        if (cameraPlaceholder) {

            cameraPlaceholder.style.display =
                "flex";
        }


        if (startCameraButton) {

            startCameraButton.disabled =
                false;
        }


        if (captureImageButton) {

            captureImageButton.disabled =
                true;
        }


        if (stopCameraButton) {

            stopCameraButton.disabled =
                true;
        }


        if (!keepCapturedImage) {

            if (capturedImage) {

                capturedImage.src =
                    "";
            }

            if (capturedImageContainer) {

                capturedImageContainer.style.display =
                    "none";
            }

            if (cameraImageInput) {

                cameraImageInput.value =
                    "";
            }

            if (analyzeImageButton) {

                analyzeImageButton.disabled =
                    true;
            }
        }


        updateCameraStatus(
            "Camera Off",
            "secondary",
            "fa-circle"
        );


        console.log(
            "Camera stopped."
        );
    }


    /* ============================================================
       CAPTURE IMAGE
       ============================================================ */

    function captureImage() {

        if (!cameraVideo) {

            alert(
                "Camera video element was not found."
            );

            return;
        }


        if (!cameraStream) {

            alert(
                "Please turn on the camera first."
            );

            return;
        }


        const videoWidth =
            cameraVideo.videoWidth;


        const videoHeight =
            cameraVideo.videoHeight;


        if (
            !videoWidth ||
            !videoHeight
        ) {

            alert(
                "Camera is not ready yet. Please wait a moment and try again."
            );

            return;
        }


        if (!cameraCanvas) {

            alert(
                "Camera canvas element was not found."
            );

            return;
        }


        /* --------------------------------------------------------
           Canvas size = actual camera resolution
           -------------------------------------------------------- */

        cameraCanvas.width =
            videoWidth;

        cameraCanvas.height =
            videoHeight;


        const context =
            cameraCanvas.getContext(
                "2d"
            );


        if (!context) {

            alert(
                "Unable to create camera capture context."
            );

            return;
        }


        /* --------------------------------------------------------
           Capture current video frame
           -------------------------------------------------------- */

        context.drawImage(
            cameraVideo,
            0,
            0,
            videoWidth,
            videoHeight
        );


        /* --------------------------------------------------------
           Show captured image
           -------------------------------------------------------- */

        const imageData =
            cameraCanvas.toDataURL(
                "image/jpeg",
                0.92
            );


        if (capturedImage) {

            capturedImage.src =
                imageData;
        }


        if (capturedImageContainer) {

            capturedImageContainer.style.display =
                "block";
        }


        /* --------------------------------------------------------
           Convert canvas to File
           -------------------------------------------------------- */

        cameraCanvas.toBlob(
            function (blob) {

                if (!blob) {

                    alert(
                        "Could not create captured image."
                    );

                    return;
                }


                if (!cameraImageInput) {

                    alert(
                        "Camera image input was not found."
                    );

                    return;
                }


                try {

                    const file =
                        new File(
                            [blob],
                            "camera_capture.jpg",
                            {
                                type:
                                    "image/jpeg",
                                lastModified:
                                    Date.now()
                            }
                        );


                    const dataTransfer =
                        new DataTransfer();


                    dataTransfer.items.add(
                        file
                    );


                    cameraImageInput.files =
                        dataTransfer.files;


                } catch (error) {

                    console.error(
                        "Could not create camera file:",
                        error
                    );

                    alert(
                        "Captured image could not be prepared for analysis."
                    );

                    return;
                }


                /* ------------------------------------------------
                   Enable Analyze
                   ------------------------------------------------ */

                if (analyzeImageButton) {

                    analyzeImageButton.disabled =
                        false;
                }


                /* ------------------------------------------------
                   Stop camera but keep captured image
                   ------------------------------------------------ */

                stopCamera(true);


                /* ------------------------------------------------
                   Restore captured status
                   ------------------------------------------------ */

                updateCameraStatus(
                    "Image Captured",
                    "success",
                    "fa-camera"
                );


                console.log(
                    "Image captured successfully."
                );

            },
            "image/jpeg",
            0.92
        );
    }


    /* ============================================================
       START CAMERA BUTTON
       ============================================================ */

    if (startCameraButton) {

        startCameraButton.addEventListener(
            "click",
            function () {

                startCamera();

            }
        );
    }


    /* ============================================================
       CAPTURE BUTTON
       ============================================================ */

    if (captureImageButton) {

        captureImageButton.addEventListener(
            "click",
            function () {

                captureImage();

            }
        );
    }


    /* ============================================================
       STOP CAMERA BUTTON
       ============================================================ */

    if (stopCameraButton) {

        stopCameraButton.addEventListener(
            "click",
            function () {

                stopCamera(true);

            }
        );
    }


    /* ============================================================
       CAMERA FORM SUBMIT
       ============================================================ */

    if (cameraDetectionForm) {

        cameraDetectionForm.addEventListener(
            "submit",
            function (event) {

                /* ------------------------------------------------
                   Check captured image
                   ------------------------------------------------ */

                if (
                    !cameraImageInput ||
                    !cameraImageInput.files ||
                    cameraImageInput.files.length === 0
                ) {

                    event.preventDefault();

                    alert(
                        "Please turn on the camera and capture an image first."
                    );

                    return;
                }


                /* ------------------------------------------------
                   Show processing message
                   ------------------------------------------------ */

                if (cameraProcessingMessage) {

                    cameraProcessingMessage.style.display =
                        "block";
                }


                /* ------------------------------------------------
                   Disable analyze button
                   ------------------------------------------------ */

                if (analyzeImageButton) {

                    analyzeImageButton.disabled =
                        true;

                    analyzeImageButton.innerHTML =
                        `
                        <span
                            class="spinner-border
                                   spinner-border-sm
                                   me-2"
                        ></span>
                        Analyzing...
                        `;
                }
            }
        );
    }


    /* ============================================================
       CLEAN CAMERA WHEN LEAVING PAGE
       ============================================================ */

    window.addEventListener(
        "beforeunload",
        function () {

            if (cameraStream) {

                cameraStream
                    .getTracks()
                    .forEach(function (track) {

                        track.stop();

                    });
            }
        }
    );


    /* ============================================================
       VIDEO DETECTION
       ============================================================ */

    const videoInput =
        document.getElementById(
            "videoInput"
        );

    const selectedVideoInfo =
        document.getElementById(
            "selectedVideoInfo"
        );

    const selectedVideoName =
        document.getElementById(
            "selectedVideoName"
        );

    const videoSizeError =
        document.getElementById(
            "videoSizeError"
        );

    const videoDetectionForm =
        document.getElementById(
            "videoDetectionForm"
        );

    const videoProcessingMessage =
        document.getElementById(
            "videoProcessingMessage"
        );

    const startVideoDetectionButton =
        document.getElementById(
            "startVideoDetectionButton"
        );


    if (videoInput) {

        videoInput.addEventListener(
            "change",
            function () {

                const file =
                    this.files[0];


                if (!file) {
                    return;
                }


                const maxSize =
                    100 *
                    1024 *
                    1024;


                if (
                    file.size >
                    maxSize
                ) {

                    if (videoSizeError) {

                        videoSizeError.style.display =
                            "block";
                    }


                    this.value =
                        "";


                    if (selectedVideoInfo) {

                        selectedVideoInfo.style.display =
                            "none";
                    }


                    return;
                }


                if (videoSizeError) {

                    videoSizeError.style.display =
                        "none";
                }


                if (selectedVideoName) {

                    selectedVideoName.textContent =
                        file.name;
                }


                if (selectedVideoInfo) {

                    selectedVideoInfo.style.display =
                        "block";
                }
            }
        );
    }


    if (videoDetectionForm) {

        videoDetectionForm.addEventListener(
            "submit",
            function () {

                if (videoProcessingMessage) {

                    videoProcessingMessage.style.display =
                        "block";
                }


                if (startVideoDetectionButton) {

                    startVideoDetectionButton.disabled =
                        true;

                    startVideoDetectionButton.innerHTML =
                        `
                        <span
                            class="spinner-border
                                   spinner-border-sm
                                   me-2"
                        ></span>
                        Processing Video...
                        `;
                }
            }
        );
    }


    /* ============================================================
       REMOVE VIDEO BUTTON
       ============================================================ */

    const removeVideoButton =
        document.getElementById(
            "removeVideoButton"
        );


    if (removeVideoButton) {

        removeVideoButton.addEventListener(
            "click",
            function () {

                const video =
                    document.querySelector(
                        "video"
                    );


                if (video) {

                    video.pause();

                    video.removeAttribute(
                        "src"
                    );

                    video.removeAttribute(
                        "srcObject"
                    );

                    video.load();
                }


                window.location.href =
                    window.location.pathname;
            }
        );
    }


    /* ============================================================
       PROCESSED VIDEO SHARE
       ============================================================ */

    const shareProcessedVideoButton =
        document.getElementById(
            "shareProcessedVideoButton"
        );


    if (shareProcessedVideoButton) {

        shareProcessedVideoButton.addEventListener(
            "click",
            async function () {

                const video =
                    document.querySelector(
                        "video"
                    );


                if (
                    navigator.share &&
                    video
                ) {

                    try {

                        await navigator.share({

                            title:
                                "SmartAgriVision AI Video",

                            text:
                                "AI processed plant detection video.",

                            url:
                                video.currentSrc ||
                                video.src ||
                                window.location.href
                        });

                    } catch (error) {

                        console.log(
                            "Share cancelled."
                        );
                    }

                } else {

                    try {

                        await navigator.clipboard.writeText(
                            window.location.href
                        );

                        alert(
                            "Page link copied to clipboard."
                        );

                    } catch (error) {

                        alert(
                            "Sharing is not supported by this browser."
                        );
                    }
                }
            }
        );
    }


    /* ============================================================
       GLOBAL SCROLL TOP BUTTON
       ============================================================ */

    const scrollTopBtn =
        document.getElementById(
            "scrollTopBtn"
        );


    if (scrollTopBtn) {

        window.addEventListener(
            "scroll",
            function () {

                if (
                    window.scrollY >
                    300
                ) {

                    scrollTopBtn.style.display =
                        "flex";

                } else {

                    scrollTopBtn.style.display =
                        "none";
                }
            }
        );


        scrollTopBtn.addEventListener(
            "click",
            function () {

                window.scrollTo({

                    top: 0,

                    behavior: "smooth"

                });
            }
        );
    }


    /* ============================================================
       AOS
       ============================================================ */

    if (
        typeof AOS !==
        "undefined"
    ) {

        AOS.init({

            duration: 1000,

            once: true

        });
    }


    /* ============================================================
       PRELOADER
       ============================================================ */

    window.addEventListener(
        "load",
        function () {

            const loader =
                document.getElementById(
                    "preloader"
                );


            if (loader) {

                loader.style.display =
                    "none";
            }
        }
    );

});