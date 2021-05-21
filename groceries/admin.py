from django.contrib import admin
from .models import Vegetable
from import_export.admin import ImportExportModelAdmin

# Register your models here.

admin.site.site_header = "Admin Page"


@admin.register(Vegetable)
class VegetableViewAdmin(ImportExportModelAdmin):
    list_display = (
        "id",
        #"UserOwner",
        "vegetable_name",
    )
    search_fields = (
    )

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    pass
