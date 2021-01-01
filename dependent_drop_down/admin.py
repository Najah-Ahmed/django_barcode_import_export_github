from django.contrib import admin

from .models import ItemModel, Category, Sub_Category

MyModels = [ItemModel, Category, Sub_Category]
admin.site.register(MyModels)
