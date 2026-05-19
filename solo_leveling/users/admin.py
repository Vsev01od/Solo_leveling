from django.contrib import admin
import django.contrib.auth.models

from users import models


class ProfileInlined(admin.TabularInline):
    model = models.Profile
    can_delete = False
    fields = ['fire_mode', 'fire_mode_bool']


class UserAdmin(django.contrib.auth.admin.UserAdmin):
    inlines = (ProfileInlined,)


admin.site.unregister(
    django.contrib.auth.models.User,
)
admin.site.register(
    django.contrib.auth.models.User,
    UserAdmin,
)
