from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Only staff or superusers can open admin dashboard
def is_admin(user):
    return user.is_staff or user.is_superuser

@user_passes_test(is_admin)
def dashboard_admin(request):
    return render(request, "admin/dashboard_final.html")
