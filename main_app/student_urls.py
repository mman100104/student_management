"""Student URLs"""
from django.urls import path
from .student_views import student_home, student_view_attendance, student_apply_leave
from .student_views import student_feedback, student_view_profile, student_fcmtoken
from .student_views import student_view_notification, student_view_result

urlpatterns = [
    path("home/", student_home, name='student_home'),
    path("view/attendance/", student_view_attendance, name='student_view_attendance'),
    path("apply/leave/", student_apply_leave, name='student_apply_leave'),
    path("feedback/", student_feedback, name='student_feedback'),
    path("view/profile/", student_view_profile, name='student_view_profile'),
    path("fcmtoken/", student_fcmtoken, name='student_fcmtoken'),
    path("view/notification/", student_view_notification, name="student_view_notification"),
    path('view/result/', student_view_result, name='student_view_result'),
]