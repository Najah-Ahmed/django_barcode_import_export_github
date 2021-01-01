
from django.urls import path

from . import views

urlpatterns = [
    path('', views.item_create_view, name='add_item'),
    path('edit/<int:pk>/', views.item_update_view, name='change_item'),
    path('ajax/sub_cat/', views.load_sub_cat, name='sub_cat'),  # AJAX
]
