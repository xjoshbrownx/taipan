from django.urls import path
from game.views import SavedGames, NewGame, Game

urlpatterns = [
    path('/', SavedGames.as_view(),name='saved_games'),
    path('/<int:pk>/<int:date>', Game.as_view(),name='game'),
    path('/new', NewGame.as_view(),name='new_game'),
]
