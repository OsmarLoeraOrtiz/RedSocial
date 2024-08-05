

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as views_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),
    path('', views_user.home_view, name='home' ),
]
