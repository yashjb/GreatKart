from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name',
                    'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',) # adding ',' is compulsory here else it will throw below error
    "the value of 'ordering' must be a list or tuple"
    # order by date joined decending

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()  # make password readonly


admin.site.register(Account, AccountAdmin)