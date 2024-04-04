from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Game, Store
from .forms import OwnerForm

# Create your views here.

def home(req):
    return render(req, 'home.html')

def about(req):
    return render(req, 'about.html')

def games_index(req):
    games = Game.objects.all() # Retrieve all games
    return render(req, 'games/index.html', 
    { 
        'games': games 
    }
)

def game_detail(req, game_id):
    game = Game.objects.get(id=game_id)
    id_list = game.store.all().values_list('id')
    stores_game_not_in = Store.objects.exclude(id__in=id_list)
    owner_form = OwnerForm()
    return render(req, 'games/detail.html', {
        'game': game, 
        'owner_form': owner_form,
        'stores': stores_game_not_in
        })

def assoc_store(req, game_id, store_id):
  Game.objects.get(id=game_id).store.add(store_id)
  return redirect('detail', game_id=game_id)

def rm_assoc_store(req, game_id, store_id):
  Game.objects.get(id=game_id).store.remove(store_id)
  return redirect('detail', game_id=game_id)

def add_owner(req, game_id):
    form = OwnerForm(req.POST)
    if form.is_valid():
        new_owner = form.save(commit=False)
        new_owner.game_id = game_id
        new_owner.save()
    return redirect('detail', game_id=game_id)

class GameCreate(CreateView):
    model = Game
    fields = '__all__'

class GameUpdate(UpdateView):
    model = Game
    fields = '__all__'

class GameDelete(DeleteView):
    model = Game
    success_url = '/games'

class StoreList(ListView):
    model = Store

class StoreCreate(CreateView):
    model = Store
    fields = "__all__"

class StoreDetail(DetailView):
    model= Store

class StoreUpdate(UpdateView):
    model = Store
    fields = ['name', 'location']

class StoreDelete(DeleteView):
    model = Store
    success_url = '/stores'