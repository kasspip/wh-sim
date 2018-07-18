from __future__ import unicode_literals

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Faction(models.Model):
    name = models.CharField(max_length=64)
    icon = models.ImageField(upload_to='faction', null=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=64)
    icon = models.ImageField(upload_to='role', null=True)

    def __str__(self):
        return self.name


class Figurine(models.Model):

    name = models.CharField(max_length=64)
    picture = models.ImageField(upload_to='figurines', null=True)
    movement = models.SmallIntegerField(default=0, validators=[MinValueValidator(0)])
    melee = models.SmallIntegerField(default=6, validators=[MinValueValidator(1), MaxValueValidator(6)])
    range = models.SmallIntegerField(default=6, validators=[MinValueValidator(1), MaxValueValidator(6)])
    strength = models.SmallIntegerField(default=1, validators=[MinValueValidator(1)])
    toughness = models.SmallIntegerField(default=1, validators=[MinValueValidator(1)])
    life = models.SmallIntegerField(default=1, validators=[MinValueValidator(1)])
    attacks = models.SmallIntegerField(default=0, validators=[MinValueValidator(0)])
    armor = models.SmallIntegerField(default=7, validators=[MinValueValidator(1), MaxValueValidator(7)])
    command = models.SmallIntegerField(default=2, validators=[MinValueValidator(2), MaxValueValidator(12)])
    invulnerability = models.SmallIntegerField(default=7, validators=[MinValueValidator(1), MaxValueValidator(7)])
    points = models.SmallIntegerField(default=1, validators=[MinValueValidator(1)])
    faction = models.ManyToManyField(Faction, related_name='figurines')
    role = models.ForeignKey(Role, related_name='figurines', null=True)

    def __str__(self):
        return self.name


class FigurineGroup(models.Model):
    figurine = models.ForeignKey(Figurine, null=True)
    count = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.figurine.name + " x " + str(self.count)


class Squad(models.Model):
    name = models.CharField(max_length=64)
    figurines = models.ManyToManyField(FigurineGroup, 'squads')

    def __str__(self):
        return self.name


class Weapon(models.Model):
    name = models.CharField(max_length=64)
