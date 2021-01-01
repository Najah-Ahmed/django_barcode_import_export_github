from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from import_export import resources
from .models import ItemModel, Category, Sub_Category

MyModels = [ItemModel, Category, Sub_Category]


class ItemResource(resources.ModelResource):
    class Meta:
        model = ItemModel
        skip_unchange = True
        report_skipped = False
        exclude = ('barcode', )


class ItemAdmin(ImportExportModelAdmin):
    resource_class = ItemResource


admin.site.register(MyModels, ItemAdmin)
