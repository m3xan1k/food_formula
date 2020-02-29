from django.urls import path
from formulas.views import DishListView, IngredientListView, DishIngredientListView

urlpatterns = [
    path('dish/', DishListView.as_view()),
    path('ingredient/', IngredientListView.as_view()),
    path('weight/', DishIngredientListView.as_view()),
]
