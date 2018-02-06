from django.db import models


class Spell(models.Model):
    name = models.CharField(max_length=100)
    spell_id = models.CharField(max_length=250)
    game_version = models.CharField(max_length=100)
    registered = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('registered',)