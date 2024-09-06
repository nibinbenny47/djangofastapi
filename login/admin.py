from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import RegisterUser

class CustomUserAdmin(UserAdmin):
    add_form = RegisterUser
    model = User
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('phone', 'date_of_birth', 'address', 'profile_image')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'phone', 'date_of_birth', 'address', 'profile_image',  'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    list_display = ('email', 'username', 'groups', 'is_staff', 'is_active')
    search_fields = ('email', 'username')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, CustomUserAdmin)