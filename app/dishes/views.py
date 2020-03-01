from rest_framework.viewsets import generics
from dishes.models import Dish, Ingredient, DishIngredientWeight
from dishes.serializers import (
    DishSerializer,
    IngredientSerializer,
    DishIngredientWeightSerializer,
)


class DishListView(generics.ListAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
