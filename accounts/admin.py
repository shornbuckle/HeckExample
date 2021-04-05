from django.contrib import admin
from .models import UserRegisterData, User
from import_export.admin import ImportExportModelAdmin

# Register your models here.

admin.site.site_header = "Admin Page"


@admin.register(User)
class UserModelAdmin(ImportExportModelAdmin):
    list_display = (
        "id",
        "email",
        "username",
        "first_name",
        "last_name",
        "city",
        "state",
        "last_login",
        "is_active",
        "is_clientuser",
        "is_superuser",
    )
    search_fields = (
        "email",
        "username",
    )
    readonly_fields = ("date_joined", "last_login")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    pass


# admin.site.register(ShelterRegisterData, RegisterShelterAdmin)
# admin.site.register(User, UserModelAdmin)
# admin.site.register(UserRegisterData, ClientUserModelAdmin)





@admin.register(UserRegisterData)
class ClientUserModelAdmin(ImportExportModelAdmin):
    list_display = (
        "user",
        "user_id",
        "user_profile_image",
    )
    search_fields = (
        "user",
        "user_id",
    )

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    pass
