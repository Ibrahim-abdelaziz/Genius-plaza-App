from django.urls import path, include
from .views import RecipeListView,RecipeView,RecipeCreateView, RecipeRetrieveUpdatdDestroy

app_name = 'Genius_app'

urlpatterns = [
    path('list/',RecipeListView.as_view()),
    path('list-user/',RecipeView.as_view()),
    path('create-recipe/',RecipeCreateView.as_view()),
    path('receipe/<int:pk>/',RecipeRetrieveUpdatdDestroy.as_view())
]