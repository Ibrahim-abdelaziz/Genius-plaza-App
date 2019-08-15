from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# one to one relationship with User.
class Recipe(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Recipe')
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

# Many to One relationship with Recipe.
class Step(models.Model):
    step_text = models.TextField()
    recipe_step = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='Recipe_Step')

# Many to One relationship with Recipe.
class Ingredient(models.Model):
    text = models.TextField()
    recipe_ingredient = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='Recipe_Ingredient')

