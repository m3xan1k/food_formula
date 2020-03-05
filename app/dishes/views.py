from rest_framework.viewsets import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from dishes.models import Dish, Ingredient, DishIngredientWeight, Category, Tag
from dishes.serializers import (
    DishFullSerializer,
    IngredientSerializer,
    CategorySerializer,
    TagSerializer,
)


class DishListView(generics.ListAPIView):
    name = 'dish-list'

    queryset = (
        Dish.objects.prefetch_related(
            'dishingredientweight_set__ingredient',
            'tags')
        .select_related('category')
        .all()
    )
    serializer_class = DishFullSerializer


class DishView(APIView):
    name = 'dish-view'

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


class IngredientListCreateView(generics.ListCreateAPIView):
    name = 'ingredient-list=create'
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()


class CategoryListCreateView(generics.ListCreateAPIView):
    name = 'category-list=create'
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class TagListCreateView(generics.ListCreateAPIView):
    name = 'tag-list=create'
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
