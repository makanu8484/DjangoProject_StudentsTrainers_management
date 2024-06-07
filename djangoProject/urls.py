"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib.auth import views
from django.urls import path, include

from userextend.forms import AuthenticationNewForm

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("intro.urls")),
    path("", include("home.urls")),
    path("", include("student.urls")),
    path("", include("trainer.urls")),
    path("", include("feedback.urls")),

    path("login/", views.LoginView.as_view(form_class=AuthenticationNewForm), name="login"),
    path("", include("django.contrib.auth.urls")),
    path("", include("userextend.urls")),
]
