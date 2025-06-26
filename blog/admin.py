from django.contrib import admin

from blog.models import Blog, CustomUser

admin.site.register(Blog)


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_staff', 'phone', 'date_joined']
    list_display_links = ['username', 'phone']
