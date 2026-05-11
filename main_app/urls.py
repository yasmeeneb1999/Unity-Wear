from django.urls import path, include
from . import views

urlpatterns = [
    # home page
    path("", views.homepage),
    # function based views
    path("items/", views.item_list),
    path("items/<int:id>/", views.item_details),
    path("items/create/", views.item_create),
    path("items/<int:id>/update", views.update_item),
    path("items/<int:id>/delete", views.delete_item),
    path("requests/create/<int:item_id>/", views.request_create),
    path("requests/", views.request_list),
    path("items/<int:id>/update", views.request_update),
    path("items/<int:id>/delete", views.request_delete),
    # class bases views --
    path("items/create/", views.ClothingItemCreateView.as_view()),
    path("items/<int:id>/update", views.ClothingItemUpdateView.as_view()),
    path("items/", views.ClothingItemListView.as_view()),
    path("items/<int:id>/", views.ClothingItemDetailView.as_view()),
    path("items/<int:id>/delete", views.ClothingItemDeleteView.as_view()),
    path("requests/", views.RequestListView.as_view()),
    path("requests/<int:id>/", views.RequestDetailView.as_view()),
    path("requests/create/", views.RequestCreateView.as_view()),
    path("requests/<int:id>/update/", views.RequestUpdateView.as_view()),
    path("requests/<int:id>/delete/", views.RequestDeleteView.as_view()),
    # path("requests/<int:id>/", views.RequestDetailView.as_view()),
    # auth sign up
    # <-- THIS: all auth views
    path("sign-up/", views.SignUpView.as_view()),
    path("auth/", include("django.contrib.auth.urls")),
]
