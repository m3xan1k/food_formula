from rest_framework.viewsets import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from dishes.models import Dish, Ingredient, DishIngredientWeight
from dishes.serializers import (
    DishFullSerializer,
)


class DishListView(generics.ListAPIView):
    queryset = (
        Dish.objects.prefetch_related(
            'dishingredientweight_set__ingredient',
            'tags')
        .select_related('category')
        .all()
    )
    serializer_class = DishFullSerializer


class DishView(APIView):
    def get(self, request, slug: str):
        instance = (
            Dish.objects
            .filter(slug__iexact=slug)
            .prefetch_related(
                'dishingredientweight_set__ingredient',
                'tags')
            .select_related('category')
        )
        if instance:
            instance = instance[0]
        serializer = DishFullSerializer(instance)
        return Response(serializer.data)
