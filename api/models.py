from django.db import models


class Pokemon(models.Model):

    name = models.CharField(max_length=255)
    type1 = models.CharField(max_length=255)
    type2 = models.CharField(max_length=255)
    total = models.IntegerField()
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    special_attack = models.IntegerField()
    special_speed = models.IntegerField()
    speed = models.IntegerField()
    generation = models.IntegerField()
    is_legendary = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Pokemon'
        verbose_name_plural = 'Pokemons'

    def __str__(self):
        return f'Pokemon {self.name} ({self.id})'
