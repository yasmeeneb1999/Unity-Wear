from django.shortcuts import render, redirect
from .models import ClothingItem, Request
from .forms import ClothingItemForm, RequestForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# 1. create view function
# 2. add view function to urls.py paths
# 3. create the template


# item list
def item_list(request):
    all_items = ClothingItem.objects.all()
    return render(request, "items/item-list.html", {"items": all_items})


# item details
def item_details(request, id):
    item = ClothingItem.objects.get(id=id)
    return render(request, "items/item-details.html", {"item": item})


# item create
def item_create(request):
    if request.method == "POST":
        print("POST request sent")
        print(f"POST/BODY {request.POST}")

        form = ClothingItemForm(request.POST)

        if form.is_valid():
            created_item = form.save(commit=False)
            created_item.owner = request.user
            created_item.save()
            return redirect(f"/items/{created_item.id}/")
    form = ClothingItemForm()
    return render(request, "items/item-form.html", {"form": form})


# item update
def update_item(request, id):
    item = ClothingItem.objects.get(id=id)
    if request.method == "POST":
        form = ClothingItemForm(request.POST, instance=item)

        if form.is_valid():
            item = form.save()
            return redirect(f"/items/{item.id}")
    form = ClothingItemForm(instance=item)
    return render(request, "items/item-form.html", {"form": form})


# create home page
def homepage(request):
    return render(request, "homepage.html")


# delete item
def delete_item(request, id):
    item = ClothingItem.objects.get(id=id)
    item.delete()
    return redirect("/items/")


# create req
def request_create(request, item_id):
    item = ClothingItem.objects.get(id=item_id)
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.requester = request.user
            new_request.clothing_item = item
            new_request.save()
            return redirect(f"/items/{item.id}/")
        form = RequestForm()
    else:
        product = ClothingItem.objects.get(id=item_id)
        form = RequestForm()
        return render(
            request,
            "requests/request-form.html",
            {"form": form, "item": item},
        )


# list req
def request_list(request):
    requests = Request.objects.all()
    return render(request, "requests/request-list.html", {"requests": requests})


# update req
def request_update(request, id):
    request_item = Request.objects.get(id=id)

    if request.user != request_item.requester:
        return redirect("/requests/")

    if request.method == "POST":
        form = RequestForm(request.POST, instance=request_item)

        if form.is_valid():
            form.save()
            return redirect("/requests/")
    else:
        form = RequestForm(instance=request_item)

    return render(request, "requests/request-form.html", {"form": form})


# delete req
def request_delete(request, request_id):
    req = Request.objects.get(id=request_id)

    if request.user != req.user:
        return redirect("/requests/")

    req.delete()
    return redirect("request_list")


# class Based Views
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)


# class create item
class ClothingItemCreateView(CreateView):
    model = ClothingItem
    form_class = ClothingItemForm
    template_name = "item/item-form.html"
    success_url = "/items/"

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


# class update item
class ClothingItemUpdateView(UpdateView):
    model = ClothingItem
    form_class = ClothingItemForm
    template_name = "item/item-form.html"
    success_url = "/items/"
    pk_url_kwarg = "id"


# class list item
class ClothingItemListView(ListView):
    model = ClothingItem
    template_name = "item/item-list.html"
    context_object_name = "items"


# class detail item
class ClothingItemDetailView(DetailView):
    model = ClothingItem
    template_name = "item/item-details.html"
    context_object_name = "item"
    pk_url_kwarg = "id"


# class delete item
class ClothingItemDeleteView(DeleteView):
    model = ClothingItem
    success_url = "/items/"
    pk_url_kwarg = "id"


# class sign-up view
class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = UserCreationForm
    success_url = "/auth/login/"


# request class
# class create req
class RequestCreateView(CreateView):
    model = Request
    form_class = RequestForm
    template_name = "requests/request-form.html"
    success_url = "/requests/"

    def form_valid(self, form):
        form.instance.requester = self.request.user
        return super().form_valid(form)


# class update req
class RequestUpdateView(UpdateView):
    model = Request
    form_class = RequestForm
    template_name = "requests/request-form.html"
    success_url = "/requests/"
    pk_url_kwarg = "id"


# class list req
class RequestListView(ListView):
    model = Request
    template_name = "requests/request-list.html"
    context_object_name = "requests"


# class detail req
class RequestDetailView(DetailView):
    model = Request
    template_name = "requests/request-details.html"
    context_object_name = "request"
    pk_url_kwarg = "id"


# class delete req
class RequestDeleteView(DeleteView):
    model = Request
    success_url = "/requests/"
    pk_url_kwarg = "id"
