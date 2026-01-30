"""Admin/HOD URLs"""
from django.urls import path
from .hod_views import admin_home, add_staff, add_course, send_student_notification
from .hod_views import send_staff_notification, add_session, admin_notify_student
from .hod_views import admin_notify_staff, admin_view_profile, check_email_availability
from .hod_views import manage_session, edit_session, student_feedback_message
from .hod_views import staff_feedback_message, view_student_leave, view_staff_leave
from .hod_views import admin_view_attendance, get_admin_attendance, add_student
from .hod_views import add_subject, manage_staff, manage_student, manage_course
from .hod_views import manage_subject, edit_staff, delete_staff, delete_course
from .hod_views import delete_subject, delete_session, delete_student, edit_student
from .hod_views import edit_course, edit_subject

urlpatterns = [
    path("home/", admin_home, name='admin_home'),
    path("staff/add", add_staff, name='add_staff'),
    path("course/add", add_course, name='add_course'),
    path("send_student_notification/", send_student_notification, name='send_student_notification'),
    path("send_staff_notification/", send_staff_notification, name='send_staff_notification'),
    path("add_session/", add_session, name='add_session'),
    path("admin_notify_student", admin_notify_student, name='admin_notify_student'),
    path("admin_notify_staff", admin_notify_staff, name='admin_notify_staff'),
    path("admin_view_profile", admin_view_profile, name='admin_view_profile'),
    path("check_email_availability", check_email_availability, name="check_email_availability"),
    path("session/manage/", manage_session, name='manage_session'),
    path("session/edit/<int:session_id>", edit_session, name='edit_session'),
    path("student/view/feedback/", student_feedback_message, name="student_feedback_message"),
    path("staff/view/feedback/", staff_feedback_message, name="staff_feedback_message"),
    path("student/view/leave/", view_student_leave, name="view_student_leave"),
    path("staff/view/leave/", view_staff_leave, name="view_staff_leave"),
    path("attendance/view/", admin_view_attendance, name="admin_view_attendance"),
    path("attendance/fetch/", get_admin_attendance, name='get_admin_attendance'),
    path("student/add/", add_student, name='add_student'),
    path("subject/add/", add_subject, name='add_subject'),
    path("staff/manage/", manage_staff, name='manage_staff'),
    path("student/manage/", manage_student, name='manage_student'),
    path("course/manage/", manage_course, name='manage_course'),
    path("subject/manage/", manage_subject, name='manage_subject'),
    path("staff/edit/<int:staff_id>", edit_staff, name='edit_staff'),
    path("staff/delete/<int:staff_id>", delete_staff, name='delete_staff'),
    path("course/delete/<int:course_id>", delete_course, name='delete_course'),
    path("subject/delete/<int:subject_id>", delete_subject, name='delete_subject'),
    path("session/delete/<int:session_id>", delete_session, name='delete_session'),
    path("student/delete/<int:student_id>", delete_student, name='delete_student'),
    path("student/edit/<int:student_id>", edit_student, name='edit_student'),
    path("course/edit/<int:course_id>", edit_course, name='edit_course'),
    path("subject/edit/<int:subject_id>", edit_subject, name='edit_subject'),
]