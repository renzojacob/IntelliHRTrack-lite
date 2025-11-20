"""
URL configuration for core project.
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from attendance.views import admin_dashboard      # your custom admin dashboard (attendance)
from main.views import dashboard_admin           # another custom admin dashboard (main)

urlpatterns = [
    # 1) Built-in Django admin
    path('admin/', admin.site.urls),

    # 2) Custom auth pages
    path('accounts/', include('accounts.urls')),

    # 3) Employee app URLs (attendance app)
    path('', include('attendance.urls')),

    # 4) Custom admin dashboards
    path('admin/dashboard/', admin_dashboard, name='admin-dashboard'),
    path('admin-panel/dashboard/', dashboard_admin, name='dashboard_admin'),

    # 5) Redirect root URL to login page
    path('', RedirectView.as_view(url='/accounts/login/', permanent=False)),
]
