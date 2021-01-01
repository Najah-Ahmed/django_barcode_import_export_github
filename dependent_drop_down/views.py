from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ItemsCreationForm
from .models import ItemModel, Sub_Category


def item_create_view(request):
    form = ItemsCreationForm()
    if request.method == 'POST':
        form = ItemsCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_item')
    return render(request, 'items/home.html', {'form': form})


def item_update_view(request, pk):
    item = get_object_or_404(ItemModel, pk=pk)
    form = ItemsCreationForm(instance=item)
    if request.method == 'POST':
        form = ItemsCreationForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('change_item', pk=pk)
    return render(request, 'items/home.html', {'form': form})


# AJAX
def load_sub_cat(request):
    category_id = request.GET.get('category_id')
    sub_cats = Sub_Category.objects.filter(category_id=category_id).all()
    return render(request, 'items/sub_cat_dropdown_list_options.html', {'sub_cats': sub_cats})
