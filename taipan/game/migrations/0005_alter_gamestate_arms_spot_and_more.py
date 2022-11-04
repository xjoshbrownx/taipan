# Generated by Django 4.1.3 on 2022-11-04 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_gamestate_arms_spot_gamestate_general_spot_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamestate',
            name='arms_spot',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='gamestate',
            name='general_spot',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='gamestate',
            name='opium_spot',
            field=models.IntegerField(default=1000),
        ),
        migrations.AlterField(
            model_name='gamestate',
            name='silk_spot',
            field=models.IntegerField(default=100),
        ),
    ]