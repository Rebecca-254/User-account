

# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# If you're using the default User model:
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
