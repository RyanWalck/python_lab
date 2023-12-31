from django.shortcuts import redirect
from django.views import View
from django.http import HttpResponse 
from django.views.generic.base import TemplateView
from .models import Pokemon
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pokemon, Moves
# Create your views here.

class Home(TemplateView):
    template_name = "home.html"
    
class About(TemplateView):
    template_name = "about.html"

class Pokemons:
    def __init__(self, name, image, bio):
        self.name = name
        self.image = image
        self.bio = bio

pokemons = [
  Pokemons("Squirtle", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/007.png",
          "When it retracts its long neck into its shell, it squirts out water with vigorous force."),
  Pokemons("Alakazam",
          "https://assets.pokemon.com/assets/cms2/img/pokedex/full/065.png", "It has an incredibly high level of intelligence. Some say that Alakazam remembers everything that ever happens to it, from birth till death."),
  Pokemons("Gengar", "https://assets.pokemon.com/assets/cms2/img/pokedex/full/094.png",
          "To steal the life of its target, it slips into the preys shadow and silently waits for an opportunity."),
  Pokemons("Mewtwo",
          "https://assets.pokemon.com/assets/cms2/img/pokedex/full/150.png", "Its DNA is almost the same as Mew’s. However, its size and disposition are vastly different."),
  Pokemons("Feraligatr",
          "https://assets.pokemon.com/assets/cms2/img/pokedex/full/160.png", "Feraligatr intimidates its foes by opening its huge mouth. In battle, it will kick the ground hard with its thick and powerful hind legs to charge at the foe at an incredible speed."),
  Pokemons("Darkrai",
          "https://assets.pokemon.com/assets/cms2/img/pokedex/full/491.png", "It chases people and Pokémon from its territory by causing them to experience deep, nightmarish slumbers."),
]

class PokemonList(TemplateView):
    template_name = "pokemon_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pokemons"] = pokemons 
        
        return context
    
class PokemonList(TemplateView):
    template_name = "pokemon_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["pokemon"] = Pokemon.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["pokemon"] = Pokemon.objects.all() 
            context["header"] = "Trending Pokemon"
        return context
    
class PokemonCreate(CreateView):
    model = Pokemon
    fields = ['name', 'img', 'bio', 'verified_pokemon']
    template_name = "pokemon_create.html"
    def get_success_url(self):
        return reverse('artist_detail', kwargs={'pk': self.object.pk})

class PokemonDetail(DetailView):
    model = Pokemon
    fields = ['name', 'img', 'bio', 'verified_pokemon']
    template_name = "pokemon_create.html"

class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = ['name', 'img', 'bio', 'verified_pokemon']
    template_name = "pokemon_update.html"
    def get_success_url(self):
        return reverse('artist_detail', kwargs={'pk': self.object.pk})
    
class PokemonDelete(DeleteView):
    model = Pokemon
    template_name = "pokemon_delete_confirmation.html"
    success_url = "/pokemons/"

class MOvesCreate(View):
    def post(self, request, pk):
        title = request.POST.get("title")
        damage = request.POST.get("damage")
        pokemon = Pokemon.objects.get(pk=pk)
        Moves.objects.create(title=title, length=length, pokemon=pokemon)
        return redirect('pokemon_detail', pk=pk)