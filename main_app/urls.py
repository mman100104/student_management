# main_app/urls.py - BỔ SUNG CÁC ROUTE THIẾU
from django.urls import path, include
from .views import login_page, doLogin, logout_user, get_attendance, showFirebaseJS

urlpatterns = [
    # ========== AUTHENTICATION ==========
    path('', login_page, name='login_page'),
    path('doLogin/', doLogin, name='user_login'),
    path('logout/', logout_user, name='user_logout'),
    path('get_attendance/', get_attendance, name='get_attendance'),
    path('firebase-messaging-sw.js', showFirebaseJS, name='showFirebaseJS'),
]

# ========== THÊM URLS CHO ADMIN/STAFF/STUDENT ==========

# Tạo các URL patterns riêng
admin_patterns = []
staff_patterns = []
student_patterns = []

# Thử import từng phần
try:
    from .hod_views import (
        admin_home, add_staff, add_course, add_session,
        manage_staff, manage_student, manage_course, manage_subject,
        add_student, add_subject, 
        # THÊM CÁC VIEW BỊ THIẾU:
        view_student_leave, view_staff_leave,  # ← THIẾU NÀY!
        student_feedback_message, staff_feedback_message,
        admin_view_attendance, get_admin_attendance,
        admin_notify_student, admin_notify_staff,
        send_student_notification, send_staff_notification,
        admin_view_profile, check_email_availability,
        edit_staff, delete_staff, delete_course, delete_subject,
        delete_session, delete_student, edit_student, edit_course, edit_subject,
        edit_session
    )
    
    admin_patterns = [
        path('admin/home/', admin_home, name='admin_home'),
        path('admin/staff/add/', add_staff, name='add_staff'),
        path('admin/course/add/', add_course, name='add_course'),
        path('admin/session/add/', add_session, name='add_session'),
        path('admin/staff/manage/', manage_staff, name='manage_staff'),
        path('admin/student/manage/', manage_student, name='manage_student'),
        path('admin/course/manage/', manage_course, name='manage_course'),
        path('admin/subject/manage/', manage_subject, name='manage_subject'),
        path('admin/student/add/', add_student, name='add_student'),
        path('admin/subject/add/', add_subject, name='add_subject'),
        
        # THÊM CÁC ROUTE BỊ THIẾU:
        path('admin/student/leave/', view_student_leave, name='view_student_leave'),
        path('admin/staff/leave/', view_staff_leave, name='view_staff_leave'),
        path('admin/student/feedback/', student_feedback_message, name='student_feedback_message'),
        path('admin/staff/feedback/', staff_feedback_message, name='staff_feedback_message'),
        path('admin/attendance/view/', admin_view_attendance, name='admin_view_attendance'),
        path('admin/attendance/fetch/', get_admin_attendance, name='get_admin_attendance'),
        path('admin/notify/student/', admin_notify_student, name='admin_notify_student'),
        path('admin/notify/staff/', admin_notify_staff, name='admin_notify_staff'),
        path('admin/send/student/notification/', send_student_notification, name='send_student_notification'),
        path('admin/send/staff/notification/', send_staff_notification, name='send_staff_notification'),
        path('admin/profile/', admin_view_profile, name='admin_view_profile'),
        path('admin/check/email/', check_email_availability, name='check_email_availability'),
        path('admin/staff/edit/<int:staff_id>/', edit_staff, name='edit_staff'),
        path('admin/staff/delete/<int:staff_id>/', delete_staff, name='delete_staff'),
        path('admin/course/delete/<int:course_id>/', delete_course, name='delete_course'),
        path('admin/subject/delete/<int:subject_id>/', delete_subject, name='delete_subject'),
        path('admin/session/delete/<int:session_id>/', delete_session, name='delete_session'),
        path('admin/student/delete/<int:student_id>/', delete_student, name='delete_student'),
        path('admin/student/edit/<int:student_id>/', edit_student, name='edit_student'),
        path('admin/course/edit/<int:course_id>/', edit_course, name='edit_course'),
        path('admin/subject/edit/<int:subject_id>/', edit_subject, name='edit_subject'),
        path('admin/session/edit/<int:session_id>/', edit_session, name='edit_session'),
    ]
    
except ImportError as e:
    print(f"Warning: Could not import admin views: {e}")

try:
    from .staff_views import (
        staff_home, staff_apply_leave, staff_feedback,
        staff_view_profile, staff_take_attendance,
        staff_update_attendance, get_students, get_student_attendance,
        save_attendance, update_attendance, staff_fcmtoken,
        staff_view_notification, staff_add_result, fetch_student_result
    )
    
    staff_patterns = [
        path('staff/home/', staff_home, name='staff_home'),
        path('staff/apply/leave/', staff_apply_leave, name='staff_apply_leave'),
        path('staff/feedback/', staff_feedback, name='staff_feedback'),
        path('staff/view/profile/', staff_view_profile, name='staff_view_profile'),
        path('staff/attendance/take/', staff_take_attendance, name='staff_take_attendance'),
        path('staff/attendance/update/', staff_update_attendance, name='staff_update_attendance'),
        path('staff/get/students/', get_students, name='get_students'),
        path('staff/attendance/fetch/', get_student_attendance, name='get_student_attendance'),
        path('staff/attendance/save/', save_attendance, name='save_attendance'),
        path('staff/attendance/update/', update_attendance, name='update_attendance'),
        path('staff/fcmtoken/', staff_fcmtoken, name='staff_fcmtoken'),
        path('staff/view/notification/', staff_view_notification, name='staff_view_notification'),
        path('staff/result/add/', staff_add_result, name='staff_add_result'),
        path('staff/result/fetch/', fetch_student_result, name='fetch_student_result'),
    ]
    
except ImportError as e:
    print(f"Warning: Could not import staff views: {e}")

try:
    from .student_views import (
        student_home, student_view_attendance, student_apply_leave,
        student_feedback, student_view_profile, student_fcmtoken,
        student_view_notification, student_view_result
    )
    
    student_patterns = [
        path('student/home/', student_home, name='student_home'),
        path('student/view/attendance/', student_view_attendance, name='student_view_attendance'),
        path('student/apply/leave/', student_apply_leave, name='student_apply_leave'),
        path('student/feedback/', student_feedback, name='student_feedback'),
        path('student/view/profile/', student_view_profile, name='student_view_profile'),
        path('student/fcmtoken/', student_fcmtoken, name='student_fcmtoken'),
        path('student/view/notification/', student_view_notification, name='student_view_notification'),
        path('student/view/result/', student_view_result, name='student_view_result'),
    ]
    
except ImportError as e:
    print(f"Warning: Could not import student views: {e}")

# Thêm tất cả vào urlpatterns chính
urlpatterns += admin_patterns + staff_patterns + student_patterns

# Thêm EditResultView nếu cần
try:
    from .edit_result_view import EditResultView
    urlpatterns.append(path('staff/result/edit/', EditResultView.as_view(), name='edit_student_result'))
except ImportError:
    pass