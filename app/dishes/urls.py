from django.urls import path
from dishes.views import DishListView, DishView, IngredientListCreateView, TagListCreateView, CategoryListCreateView

urlpatterns = [
    path('dishes/dish/', DishListView.as_view(), name=DishListView.name),
    path('dishes/dish/<str:slug>/', DishView.as_view(), name=DishView.name),
    path('dishes/ingredients/', IngredientListCreateView.as_view(),
         name=IngredientListCreateView.name),
    path('dishes/tags/', TagListCreateView.as_view(),
         name=TagListCreateView.name),
    path('dishes/categories/', CategoryListCreateView.as_view(),
         name=CategoryListCreateView.name),
]
