from django.db import models
from django.conf import settings

# Create your models here.
class Game(models.Model):

    DEBT = 'D'
    GUNS = 'G'
    DOB = [(DEBT,'Debt'),(GUNS,'Guns')]

    player = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name = ("player"), on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    debt_or_guns = models.CharField(choices=DOB, default='D', max_length=1)

    # def save(self):
    #     init_game = GameState()
    #     init_game.save()
    #     return super().save()

    def initialize(self):
        if self.debt_or_guns == 'G':
            init_game = GameState(game=self,debt=0,cash=0,guns=5)
        else:
            init_game = GameState(game=self)
        init_game.save()
        

class GameState(models.Model):
    
    HONGKONG = 'HK'
    SHANGHAI = 'SH'
    NAGASAKI = 'NS'
    SAIGON = 'SG'
    MANILA = 'MN'
    SINGAPORE = 'SP'
    BATAVIA = 'BV'

    LOCATIONS = [
        (HONGKONG,'Hong Kong'),
        (SHANGHAI,'Shanghai'),
        (NAGASAKI,'Nagasaki'),
        (SAIGON,'Saigon'),
        (MANILA,'Manila'),
        (SINGAPORE,'Singapore'),
        (BATAVIA,'Batavia'),
    ]

    JAN = 1
    FEB = 2
    MAR = 3
    APR = 4
    MAY = 5
    JUN = 6
    JUL = 7
    AUG = 8
    SEP = 9
    OCT = 10
    NOV = 11
    DEC = 12

    MONTHS = [
        (JAN,'January'),
        (FEB,'February'),
        (MAR,'March'),
        (APR,'April'),
        (MAY,'May'),
        (JUN,'June'),
        (JUL,'July'),
        (AUG,'August'),
        (SEP,'September'),
        (OCT,'October'),
        (NOV,'November'),
        (DEC,'December'),
    ]

    game = models.ForeignKey(Game, related_name='game_state', on_delete=models.CASCADE)
    current_location = models.CharField(choices=LOCATIONS, max_length=2, default=HONGKONG)
    date = models.IntegerField(default=0)
    month = models.IntegerField(default=1, choices=MONTHS)
    year = models.IntegerField(default=1860)
    ship_health = models.IntegerField(default=100)
    ship_size = models.IntegerField(default=60)
    guns = models.IntegerField(default=0)
    cash = models.IntegerField(default=500)
    bank = models.IntegerField(default=0)
    debt = models.IntegerField(default=500)
    opium_ship = models.IntegerField(default=0)
    silk_ship = models.IntegerField(default=0)
    arms_ship = models.IntegerField(default=0)
    general_ship = models.IntegerField(default=0)
    vacant_ship = models.IntegerField(default=60)
    opium_wh = models.IntegerField(default=0)
    silk_wh = models.IntegerField(default=0)
    arms_wh = models.IntegerField(default=0)
    general_wh = models.IntegerField(default=0)
    vacant_wh = models.IntegerField(default=10000)
    opium_spot = models.IntegerField(default=1000)
    silk_spot = models.IntegerField(default=100)
    arms_spot = models.IntegerField(default=10)
    general_spot = models.IntegerField(default=1)
    x_points = models.IntegerField(default=0)

