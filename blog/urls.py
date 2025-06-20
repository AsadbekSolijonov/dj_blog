from django.urls import path
from blog import views as blog_views

urlpatterns = [
    path('', blog_views.home, name='home'),
    path('in_actives', blog_views.in_active, name='in_active_blogs'),
    path('<int:blog_id>/view', blog_views.detail, name='detail'),
    path('about/', blog_views.about, name='about'),
    path('<int:blog_id>/update', blog_views.update, name='update'),
]
