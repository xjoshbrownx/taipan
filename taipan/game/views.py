from django.shortcuts import render
from django.views.generic import DetailView, FormView, ListView
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from game.forms import NewGame
from game.models import GameState, Game

# Create your views here.
class SavedGames(LoginRequiredMixin, ListView):
    model = get_user_model()
    context_object_name = 'user'
    template_name = 'saved_games.html'



class NewGame(FormView):
    template_name = 'new_game.html'
    form_class = NewGame
    # success_url = ''

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        return super().form_valid(form)

class Game(DetailView):
    context_object_name: str = 'game'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["game_state"] = GameState.objects.filter(date=self.request)
        return context
    