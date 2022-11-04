from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView, ListView, CreateView, FormView 
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from game.forms import NewGame
from game.models import GameState, Game

# Create your views here.
class SavedGames(LoginRequiredMixin, ListView):
    # model = Game
    context_object_name = 'games'
    template_name = 'game/saved_games.html'

    def get_queryset(self):
        return Game.objects.filter(player=self.request.user).prefetch_related('game_state')

    # def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     context['gamestate'] = self.object.game_state.last()

class NewGame(CreateView):
    model = Game
    fields = ['company_name', 'debt_or_guns']

    def get_success_url(self):
        return reverse('game', kwargs = {'pk':self.object.id,'date':0})

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        form.instance.player = self.request.user # It should return an HttpResponse.
        out = super().form_valid(form) 
        self.object.initialize()
        # print(self.request.user.id)
        return out

class GameView(DetailView):
    context_object_name: str = 'game'
    template_name = 'game/game.html'

    def get_object(self):
        out = GameState.objects.get(game__id = self.kwargs.get('pk'),date = self.kwargs.get('date'))
        # print(dict(out))
        return out

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["user"] = self.request.user
    #     return context
    