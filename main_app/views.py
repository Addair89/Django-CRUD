from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game

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
    return render(req, 'games/detail.html', {'game': game})

class GameCreate(CreateView):
    model = Game
    fields = '__all__'

class GameUpdate(UpdateView):
    model = Game
    fields = '__all__'

class GameDelete(DeleteView):
    model = Game
    success_url = '/games'