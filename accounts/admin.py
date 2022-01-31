from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class MyUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Custom', {'fields': ('screen_name',)}),
    )

admin.site.register(User, MyUserAdmin)
