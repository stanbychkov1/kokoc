from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


class UserAdminCustom(UserAdmin):
    fieldsets = (
        (None,
         {'fields': ('username', 'password')}),
        (_('Personal info'),
         {'fields': ('first_name', 'last_name', 'email', 'balance',
                     'background_color', 'username_color',
                     'passed_test_quantity')}),
        (_('Permissions'),
         {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups',
                     'user_permissions',)}),
        (_('Important dates'),
         {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email',  'is_staff', 'is_superuser',)
    list_filter = ('username', 'email', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')


admin.site.register(get_user_model(), UserAdminCustom)
