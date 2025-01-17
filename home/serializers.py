from rest_framework import serializers
from .models import *

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"

class ReceipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipe
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['ingredients'] = IngredientSerializer(instance.ingredients.all(), many=True).data
        return representation