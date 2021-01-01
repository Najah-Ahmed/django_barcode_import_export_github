from django.db import models

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Sub_Category(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class ItemModel(models.Model):
    item_name = models.CharField(max_length=124)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True)
    sub_category = models.ForeignKey(
        Sub_Category, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.item_name
