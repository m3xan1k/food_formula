from django.urls import path
from dishes.views import DishListView, DishView, IngredientListCreateView, TagListCreateView, CategoryListCreateView

urlpatterns = [
    path('dishes/dish/', DishListView.as_view()),
    path('dishes/dish/<str:slug>/', DishView.as_view()),
    path('dishes/ingredients/', IngredientListCreateView.as_view()),
    path('dishes/tags/', TagListCreateView.as_view()),
    path('dishes/categories/', CategoryListCreateView.as_view()),
]
