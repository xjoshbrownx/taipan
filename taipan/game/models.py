from django.db import models
from django.conf import settings

# Create your models here.
class Game(models.Model):

    DEBT = 'D'
    GUNS = 'G'
    DOB = [(DEBT,'Debt'),(GUNS,'Guns')]

    player = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name = ("player"), on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50)
    debt_or_guns = models.CharField(choices=DOB, max_length=1)

    

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

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    current_location = models.CharField(choices=LOCATIONS, max_length=2, default=HONGKONG)
    date = models.IntegerField(default=0)
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
    opium_wh = models.IntegerField(default=0)
    silk_wh = models.IntegerField(default=0)
    arms_wh = models.IntegerField(default=0)
    general_wh = models.IntegerField(default=0)
    x_points = models.IntegerField(default=0)