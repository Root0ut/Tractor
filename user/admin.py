from django.contrib import admin
from user.models import UserLoginLog


class UserLoginLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'ip_address', 'user_agent',)
    list_filter = ('ip_address',)
    date_hierarchy = 'created'


admin.site.register(UserLoginLog, UserLoginLogAdmin)
