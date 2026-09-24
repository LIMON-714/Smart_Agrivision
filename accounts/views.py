from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.db.models import Avg

from .forms import (
    RegisterForm,
    UserUpdateForm,
    ProfileUpdateForm,
    CustomPasswordChangeForm,
)

from .models import Profile

# Detection app model
from detection.models import DetectionHistory


# =========================================================
# LOGIN VIEW
# =========================================================

def login_view(request):

    # Already logged-in users don't need to see login page
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        username = request.POST.get(
            "username",
            ""
        ).strip()

        password = request.POST.get(
            "password",
            ""
        )

        if not username or not password:

            messages.error(
                request,
                "Please enter username and password."
            )

            return render(
                request,
                "User_auth/login.html",
            )

        # Authenticate user

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        # Login successful

        if user is not None:

            login(
                request,
                user
            )

            messages.success(
                request,
                "Login successful."
            )

            return redirect("home")

        messages.error(
            request,
            "Invalid username or password."
        )

    return render(
        request,
        "User_auth/login.html",
    )


# =========================================================
# REGISTER VIEW
# =========================================================

def register_view(request):

    # Already logged-in users don't need registration page
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        form = RegisterForm(
            request.POST
        )

        if form.is_valid():

            user = form.save()

            phone = request.POST.get(
                "phone",
                ""
            ).strip()

            country = request.POST.get(
                "country",
                ""
            ).strip()

            # Get existing Profile or create one
            profile, created = Profile.objects.get_or_create(
                user=user
            )

            if phone:
                profile.phone = phone

            if country:
                profile.country = country

            profile.save()

            messages.success(
                request,
                "Registration successful. Please login."
            )

            return redirect("login")

        else:

            print("REGISTER FORM ERRORS:")
            print(form.errors)

            messages.error(
                request,
                "Please correct the errors in the registration form."
            )

    else:

        form = RegisterForm()

    return render(
        request,
        "User_auth/register.html",
        {
            "form": form,
        },
    )


# =========================================================
# LOGOUT VIEW
# =========================================================

@require_POST
@login_required
def logout_view(request):

    logout(request)

    messages.success(
        request,
        "Logged out successfully."
    )

    return redirect("login")


# =========================================================
# PROFILE VIEW
# =========================================================

@login_required
def profile_view(request):

    # -----------------------------------------------------
    # GET OR CREATE PROFILE
    # -----------------------------------------------------

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    # -----------------------------------------------------
    # USER-SPECIFIC DETECTION HISTORY
    # -----------------------------------------------------

    detections = (
        DetectionHistory.objects
        .filter(user=request.user)
        .order_by("-created_at")
    )

    # -----------------------------------------------------
    # TOTAL DETECTIONS
    # -----------------------------------------------------

    total_detections = detections.count()

    # -----------------------------------------------------
    # RECENT DETECTIONS
    # -----------------------------------------------------

    recent_detections = detections[:10]

    # -----------------------------------------------------
    # HEALTHY COUNT
    # -----------------------------------------------------

    healthy_count = detections.filter(
        predicted_class__icontains="healthy"
    ).count()

    # -----------------------------------------------------
    # PROCESSING COUNT
    # -----------------------------------------------------

    pending_count = detections.filter(
        predicted_class="Processing..."
    ).count()

    # -----------------------------------------------------
    # DISEASE COUNT
    # Everything except healthy and processing
    # -----------------------------------------------------

    disease_count = (
        total_detections
        - healthy_count
        - pending_count
    )

    # Safety check
    if disease_count < 0:
        disease_count = 0

    # -----------------------------------------------------
    # PERCENTAGES
    # -----------------------------------------------------

    if total_detections > 0:

        healthy_percentage = round(
            (healthy_count / total_detections) * 100,
            2
        )

        disease_percentage = round(
            (disease_count / total_detections) * 100,
            2
        )

        pending_percentage = round(
            (pending_count / total_detections) * 100,
            2
        )

    else:

        healthy_percentage = 0
        disease_percentage = 0
        pending_percentage = 0

    # -----------------------------------------------------
    # AVERAGE CONFIDENCE
    #
    # This is average prediction confidence,
    # NOT actual model accuracy.
    # -----------------------------------------------------

    average_confidence = detections.exclude(
        predicted_class="Processing..."
    ).aggregate(
        average=Avg("confidence")
    )["average"]

    if average_confidence is None:
        average_confidence = 0

    accuracy = round(
        float(average_confidence),
        2
    )

    # -----------------------------------------------------
    # TOTAL REPORTS
    #
    # No Report model provided yet.
    # -----------------------------------------------------

    total_reports = 0

    # =====================================================
    # PROFILE COMPLETION
    # =====================================================
    #
    # Real data based on User + Profile fields.
    #
    # Each completed field gets equal weight.
    # Empty fields are not counted.
    #
    # You can add/remove fields from this list depending
    # on your Profile model.
    # =====================================================

    profile_fields = [

        # Django User fields
        request.user.first_name,
        request.user.last_name,
        request.user.email,

        # Profile fields
        profile.profile_image,
        profile.cover_image,
        profile.phone,
        profile.date_of_birth,
        profile.gender,
        profile.language,
        profile.theme,
        profile.address,
        profile.district,
        profile.division,
        profile.country,
        profile.postal_code,
        profile.bio,

    ]

    # Total number of fields
    total_profile_fields = len(profile_fields)

    # Count completed fields
    completed_profile_fields = 0

    for field in profile_fields:

        if field:

            completed_profile_fields += 1

    # Calculate percentage
    if total_profile_fields > 0:

        profile_completion = round(
            (
                completed_profile_fields
                / total_profile_fields
            ) * 100
        )

    else:

        profile_completion = 0

    # -----------------------------------------------------
    # PLACEHOLDER DATA
    #
    # These require separate models.
    # -----------------------------------------------------

    achievements = []

    recent_activities = []

    latest_reports = []

    favorite_crops = []

    # -----------------------------------------------------
    # CONTEXT
    # -----------------------------------------------------

    context = {

        # Profile
        "profile":
            profile,

        # -------------------------------------------------
        # Detection statistics
        # -------------------------------------------------

        "total_detections":
            total_detections,

        "healthy_count":
            healthy_count,

        "disease_count":
            disease_count,

        "pending_count":
            pending_count,

        "total_reports":
            total_reports,

        # -------------------------------------------------
        # Average confidence
        # -------------------------------------------------

        "accuracy":
            accuracy,

        # -------------------------------------------------
        # Detection percentages
        # -------------------------------------------------

        "healthy_percentage":
            healthy_percentage,

        "disease_percentage":
            disease_percentage,

        "pending_percentage":
            pending_percentage,

        # -------------------------------------------------
        # Detection history
        # -------------------------------------------------

        "recent_detections":
            recent_detections,

        # -------------------------------------------------
        # Profile completion
        # -------------------------------------------------

        "profile_completion":
            profile_completion,

        # Optional detailed completion data
        "completed_profile_fields":
            completed_profile_fields,

        "total_profile_fields":
            total_profile_fields,

        # -------------------------------------------------
        # Other sections
        # -------------------------------------------------

        "achievements":
            achievements,

        "recent_activities":
            recent_activities,

        "latest_reports":
            latest_reports,

        "favorite_crops":
            favorite_crops,
    }

    # -----------------------------------------------------
    # RENDER
    # -----------------------------------------------------

    return render(
        request,
        "User_auth/profile.html",
        context,
    )


# =========================================================
# EDIT PROFILE VIEW
# =========================================================

@login_required
def profile_edit(request):

    # -----------------------------------------------------
    # GET OR CREATE PROFILE
    # -----------------------------------------------------

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    # -----------------------------------------------------
    # POST REQUEST
    # -----------------------------------------------------

    if request.method == "POST":

        user_form = UserUpdateForm(
            request.POST,
            instance=request.user
        )

        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        # -------------------------------------------------
        # VALIDATION
        # -------------------------------------------------

        if (
            user_form.is_valid()
            and profile_form.is_valid()
        ):

            # Save User information
            user_form.save()

            # Save Profile information
            profile_form.save()

            messages.success(
                request,
                "Your profile has been updated successfully."
            )

            return redirect("profile")

        else:

            print("USER FORM ERRORS:")
            print(user_form.errors)

            print("PROFILE FORM ERRORS:")
            print(profile_form.errors)

            messages.error(
                request,
                "Please correct the errors in the form."
            )

    # -----------------------------------------------------
    # GET REQUEST
    # -----------------------------------------------------

    else:

        user_form = UserUpdateForm(
            instance=request.user
        )

        profile_form = ProfileUpdateForm(
            instance=profile
        )

    # -----------------------------------------------------
    # RENDER
    # -----------------------------------------------------

    return render(
        request,
        "User_auth/edit_profile.html",
        {
            "user_form":
                user_form,

            "profile_form":
                profile_form,
        },
    )


# =========================================================
# CHANGE PASSWORD VIEW
# =========================================================

@login_required
def change_password_view(request):

    # -----------------------------------------------------
    # POST REQUEST
    # -----------------------------------------------------

    if request.method == "POST":

        form = CustomPasswordChangeForm(
            user=request.user,
            data=request.POST
        )

        if form.is_valid():

            # Save new password
            user = form.save()

            # Keep user logged in after password change
            update_session_auth_hash(
                request,
                user
            )

            messages.success(
                request,
                "Your password has been changed successfully."
            )

            return redirect("profile")

        else:

            print("PASSWORD FORM ERRORS:")
            print(form.errors)

            messages.error(
                request,
                "Please correct the password errors."
            )

    # -----------------------------------------------------
    # GET REQUEST
    # -----------------------------------------------------

    else:

        form = CustomPasswordChangeForm(
            user=request.user
        )

    # -----------------------------------------------------
    # RENDER
    # -----------------------------------------------------

    return render(
        request,
        "User_auth/change_password.html",
        {
            "form": form,
        },
    )


# =========================================================
# DELETE ACCOUNT VIEW
# =========================================================

@login_required
def delete_account_view(request):

    if request.method == "POST":

        user = request.user

        # Logout before deleting user
        logout(request)

        # Delete User
        #
        # Profile and DetectionHistory use CASCADE,
        # so related records will also be deleted.

        user.delete()

        messages.success(
            request,
            "Your account has been deleted successfully."
        )

        return redirect("login")

    return redirect("profile")

