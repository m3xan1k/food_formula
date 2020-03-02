from django.urls import path
from dishes.views import DishListView

urlpatterns = [
    path('dishes/dish/', DishListView.as_view()),
]
