from rest_framework import serializers
from .models import *
from django.template.defaultfilters import slugify
import uuid

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

class CreateReceipeSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    receipe_ingredients = serializers.ListField(
        child=serializers.CharField(max_length=255),
        write_only=True
    )
    
    class Meta:
        model = Receipe
        fields = "__all__"

    def create(self, validated_data):
        receipe_ingredients = validated_data.pop('receipe_ingredients', [])
        slug = slugify(validated_data['title'])
        if Receipe.objects.filter(slug=slug).exists():
            slug += "-" + str(uuid.uuid4())
        receipe = Receipe.objects.create(
            title=validated_data['title'],
            instructions=validated_data['instructions'],
            #image=validated_data['image'],
            slug=slug,
            rtype=validated_data['rtype']
        )
        for ri in receipe_ingredients:
            Ingredient.objects.get_or_create(recipe=receipe, name=ri)
            
        return receipe

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['receipe_ingredients'] = IngredientSerializer(instance.ingredients.all(), many=True).data
        return representation