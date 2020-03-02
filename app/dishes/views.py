from rest_framework.viewsets import generics
from dishes.models import Dish, Ingredient, DishIngredientWeight
from dishes.serializers import (
    DishFullSerializer,
)


class DishListView(generics.ListAPIView):

    queryset = Dish.objects.prefetch_related(
        'dishingredientweight_set__ingredient',
        'tags')\
        .select_related('category')\
        .all()

    serializer_class = DishFullSerializer
