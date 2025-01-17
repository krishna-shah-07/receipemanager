from django.db import models

# Create your models here.

class Receipe(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    instructions = models.TextField()    
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True) 
    rtype = models.CharField(choices=[("veg", "Vegetarian"), ("non-veg", "Non-Vegetarian")], max_length=10)

    def __str__(self):
        return self.title
    
class Ingredient(models.Model):
    recipe = models.ForeignKey(Receipe, on_delete=models.CASCADE, related_name="ingredients")
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.name