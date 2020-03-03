from django.urls import path
from dishes.views import DishListView, DishView

urlpatterns = [
    path('dishes/dish/', DishListView.as_view()),
    path('dishes/dish/<str:slug>/', DishView.as_view()),
]
