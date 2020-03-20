from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List


def home_page(request):
    return render(request, "home.html")


def view_list(request, list_id):
    list1 = List.objects.get(id=list_id)
    return render(request, "list.html", {"list": list1})


def new_list(request):
    list1 = List.objects.create()
    Item.objects.create(
        text=request.POST["item_text"], list=list1
    )
    return redirect(f"/lists/{list1.id}/")


def add_item(request, list_id):
    list1 = List.objects.get(id=list_id)
    Item.objects.create(
        text=request.POST["item_text"], list=list1
    )
    return redirect(f"/lists/{list1.id}/")


def show_all_lists(request):
    # custom
    return HttpResponse(List.objects.all().values_list())
