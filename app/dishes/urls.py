from django.urls import path
from dishes.views import DishListView

urlpatterns = [
    path('dish/', DishListView.as_view()),
]
