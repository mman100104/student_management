"""Staff URLs"""
from django.urls import path
from .staff_views import staff_home, staff_apply_leave, staff_feedback, staff_view_profile
from .staff_views import staff_take_attendance, staff_update_attendance, get_students
from .staff_views import get_student_attendance, save_attendance, update_attendance
from .staff_views import staff_fcmtoken, staff_view_notification, staff_add_result, fetch_student_result
from .edit_result_view import EditResultView

urlpatterns = [
    path("home/", staff_home, name='staff_home'),
    path("apply/leave/", staff_apply_leave, name='staff_apply_leave'),
    path("feedback/", staff_feedback, name='staff_feedback'),
    path("view/profile/", staff_view_profile, name='staff_view_profile'),
    path("attendance/take/", staff_take_attendance, name='staff_take_attendance'),
    path("attendance/update/", staff_update_attendance, name='staff_update_attendance'),
    path("get_students/", get_students, name='get_students'),
    path("attendance/fetch/", get_student_attendance, name='get_student_attendance'),
    path("attendance/save/", save_attendance, name='save_attendance'),
    path("attendance/update/", update_attendance, name='update_attendance'),
    path("fcmtoken/", staff_fcmtoken, name='staff_fcmtoken'),
    path("view/notification/", staff_view_notification, name="staff_view_notification"),
    path("result/add/", staff_add_result, name='staff_add_result'),
    path("result/edit/", EditResultView.as_view(), name='edit_student_result'),
    path('result/fetch/', fetch_student_result, name='fetch_student_result'),
]