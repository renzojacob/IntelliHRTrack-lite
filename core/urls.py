"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from attendance.views import admin_dashboard


urlpatterns = [
    # 1) Keep built-in admin on /admin/
    path('admin/', admin.site.urls),

    # 2) Put your custom auth pages under /accounts/
    path('accounts/', include('accounts.urls')),

    # 3) Include attendance app URLs (these define employee/dashboard/ etc.)
    path('', include('attendance.urls')),

    # 4) Redirect the empty root URL to the login page
    path('', RedirectView.as_view(url='/accounts/login/', permanent=False)),
        path("admin/dashboard/", admin_dashboard, name="admin-dashboard"),

]

