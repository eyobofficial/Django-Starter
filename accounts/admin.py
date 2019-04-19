from django.contrib import admin

from .models import CustomUser, Profile


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'is_active',
        'is_staff',
        'is_superuser',
        'last_login'
    )
    list_display_link = ('username', 'email')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'first_name', 'last_name')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', )
