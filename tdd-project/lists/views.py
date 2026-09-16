from django.shortcuts import render
from lists.models import List, Item


def home_page(request):
    if request.method == 'POST':
        list_ = List.objects.create()
        Item.objects.create(text=request.POST['item_text'], list=list_)
        return render(request, 'lists/list.html', {'list': list_})

    return render(request, 'lists/home.html')


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'lists/list.html', {'list': list_})