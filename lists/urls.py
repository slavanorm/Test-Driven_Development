from django.urls import path
from lists import views

urlpatterns = [
    path("<int:list_id>/", views.view_list),
    path("new", views.new_list),
    path("<int:list_id>/add_item", views.add_item),
    # custom
    path("", views.show_all_lists),
]
