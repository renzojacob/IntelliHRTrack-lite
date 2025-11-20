from django.urls import path
from .views import employee_dashboard, admin_dashboard
from .views import capture_attendance

urlpatterns = [
    path('employee/dashboard/', employee_dashboard, name='employee_dashboard'),
    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),
    path('capture/', capture_attendance, name='capture_attendance'),
]
