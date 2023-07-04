from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('pokemons/', views.PokemonList.as_view(), name="pokemon_list"),
    path('pokemons/new/', views.PokemonCreate.as_view(), name="pokemon_create"),
    path('pokemons/<int:pk>/', views.PokemonDetail.as_view(), name="pokemon_detail"),
    path('pokemons/<int:pk>/update',views.PokemonUpdate.as_view(), name="pokemon_update"),
    path('artists/<int:pk>/delete',views.PokemonDelete.as_view(), name="pokemon_delete"),

]
