from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("kwt_home.urls")),
    path("about/", include("kwt_about.urls")),
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),    
    path("booking/", include("kwt_appointment.urls")),
    path("browse/", include("kwt_gallery.urls")),
    path("misc/", include("kwt_misc.urls")),
    path("users/", include('django.contrib.auth.urls')),
    path("users/", include("kwt_users.urls")),
]
