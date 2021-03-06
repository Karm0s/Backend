from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from .forms import UserAdminChangeForm, UserAdminCreationForm
from .models import User

class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm


    list_display = ('email', 'admin')
    list_filter =  ('admin', )
    fieldsets = (
        (
            None, {"fields": ('username', 'email', 'password', 'active')}
        ),
        (
            'Permissions', {"fields":('admin', )},
        )
    )

    search_fields = ('email', )
    ordering = ('email', )
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

admin.site.unregister(Group)

    


