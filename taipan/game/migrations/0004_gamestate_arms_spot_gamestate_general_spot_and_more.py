# Generated by Django 4.1.3 on 2022-11-04 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_gamestate_month_gamestate_opium_spot_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamestate',
            name='arms_spot',
            field=models.IntegerField(default=5000),
        ),
        migrations.AddField(
            model_name='gamestate',
            name='general_spot',
            field=models.IntegerField(default=5000),
        ),
        migrations.AddField(
            model_name='gamestate',
            name='silk_spot',
            field=models.IntegerField(default=5000),
        ),
    ]