from django.urls import path
from dishes.views import (
    DishListView,
    DishView,
    IngredientListCreateView,
    TagListCreateView,
    CategoryListCreateView,
)
from django.views.generic import TemplateView

urlpatterns = [
    path('front/', TemplateView.as_view(template_name='dishes/index.html')),
    path("dishes/dish/", DishListView.as_view(), name=DishListView.name),
    path("dishes/dish/<str:slug>/", DishView.as_view(), name=DishView.name),
    path(
        "dishes/ingredients/",
        IngredientListCreateView.as_view(),
        name=IngredientListCreateView.name,
    ),
    path("dishes/tags/", TagListCreateView.as_view(), name=TagListCreateView.name),
    path(
        "dishes/categories/",
        CategoryListCreateView.as_view(),
        name=CategoryListCreateView.name,
    ),
]
