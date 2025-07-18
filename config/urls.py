from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    # User registration
    path('register/', blog_views.register, name='register'),

    # User login
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', blog_views.site_logout, name='site_logout'),
    path('ask_login/', blog_views.ask_login, name='ask_login'),
    path('profile/', blog_views.profile, name='profile'),
    path('change/', blog_views.change_profile, name='change_profile')

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
