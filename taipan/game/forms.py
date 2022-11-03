from django.forms import ModelForm
from game.models import Game

class NewGame(ModelForm):
    class Meta:
        model = Game
        fields = ['company_name', 'debt_or_guns']