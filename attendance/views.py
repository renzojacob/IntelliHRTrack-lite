from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


@login_required
def employee_dashboard(request):
    return render(request, 'employee/dashboard.html')

@login_required
def admin_dashboard(request):
    return render(request, 'admin/dashboard_final.html')

@staff_member_required
def admin_dashboard(request):
    return render(request, "admin/dashboard_final.html")
