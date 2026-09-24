from django.urls import path
from . import views

urlpatterns = [
    # Login
    path('login/', views.login_view, name='login'),

    # Register
    path('register/', views.register_view, name='register'),

    # Logout
    path('logout/', views.logout_view, name='logout'),

    # Profile
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path("change-password/",views.change_password_view,name="change_password"),
    path("delete-account/",views.delete_account_view,name="delete_account"),

]