from django.urls import path
from . import views

urlpatterns = [
    # Register New Mmber
    path('new-member-registration',
         views.registerNewMember,
         name="new-member-registration"),
    # All Members
    path('all-members/', views.allMembers, name="all-members"),
    # Profile Details
    path('profile-details/<int:profile_id>',
         views.showprofiledetails,
         name="profile-details"),
    # Update Member
    path('update-member-admin/<int:slug_id>',
         views.UpdateMemberAdmin,
         name="update-member-admin"),
    # Search
    path('search-member/', views.search_member, name="search-member"),
    # Payments
    path('payments/<slug:slug_id>', views.payments, name="payments"),
    # Burials
    path('burials/<slug:slug_id>', views.burials, name="member-burials"),
    path('list-burials', views.allburials, name="all-member-burials"),

    ### -----------------Pending Member-------------------- ####
    # Pending Member View
    path('view-pending/<str:slug_id>/',
         views.PendingMemberDetail,
         name="view-pending"),
    # Pending Update
    path('update_pending_member/<str:slug_id>/',
         views.UpdatePendingMember,
         name="update_pending_member"),
]
