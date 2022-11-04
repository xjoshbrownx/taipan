from django.urls import path
from game.views import SavedGames, NewGame, GameView

urlpatterns = [
    path('', SavedGames.as_view(),name='saved_games'),
    path('<int:pk>/<int:date>', GameView.as_view(),name='game'),
    path('new/', NewGame.as_view(),name='new_game'),
]
