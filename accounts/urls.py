from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Register
    path('register', views.registerMember, name="register"),
    # Login
    path('login', views.loginMember, name="login"),
    # Logout
    path('logout', views.logoutUser, name="logout"),
    # Homepage
    path('homepage', views.homepage, name="homepage"),
    # Member Profile Details
    path('member-details/<slug:slug_id>',
         views.memberDetails,
         name="member-details"),
    # Package Details
    path('member-package/<slug:slug_id>',
         views.memberPackage,
         name="member-package"),
    # Member Documets
    path('member-documents/<slug:slug_id>',
         views.memberDocuments,
         name="member-documents"),
    # Member Payments
    path('member-payments/<slug:slug_id>',
         views.memberPayments,
         name="member-payments"),

    ### -----------------PASSWORD RESET-------------------- ####
    path('reset_password/',
         auth_views.PasswordResetView.as_view(
             template_name="accounts/password_reset.html"),
         name="reset_password"),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(
             template_name="accounts/password_reset_sent.html"),
         name="password_reset_done"),
    path('reset<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="accounts/password_reset_form.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name="accounts/password_reset_done.html"),
         name="password_reset_complete"),
]
