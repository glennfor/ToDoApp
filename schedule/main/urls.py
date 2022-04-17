from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Index"),
    path('home/', views.home, name="Home"),
    path('<int:id>', views.viewItem, name="View List"),
    path('view/', views.viewList, name="View List"),
    path("create/", views.create, name="Create"),
    path("delete/list/<int:id>", views.deleteList, name="Delete List"),
    path("delete/item/<int:list_id>/<str:txt>", views.deleteItem, name="Delete Item"),
]
