from __future__ import unicode_literals

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from home import choices


class Race(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
    

class Army(models.Model):
    name = models.CharField(max_length=64)
    icon = models.ImageField(upload_to='faction', null=True)
    race = models.ForeignKey(Race,  null=True)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=64)
    icon = models.ImageField(upload_to='role', null=True)
    display_order = models.SmallIntegerField(default=0)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return self.name


class Keyword(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=64)
    power = models.SmallIntegerField(default=0, validators=[MinValueValidator(0)])
    role = models.ForeignKey(Role, null=True)
    army = models.ForeignKey(Army, related_name='figurines', null=True)
    image = models.ImageField(upload_to='uploaded_images', null=True, blank=True)

    def __str__(self):
        return self.name


class Weapon(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class DegressiveProfile(models.Model):
    life_1 = models.CharField(max_length=32, choices=choices.LargeNumericalEnum.CHOICES, default=choices.LargeNumericalEnum.ZERO)
    life_2 = models.CharField(max_length=32, choices=choices.LargeNumericalEnum.CHOICES, default=choices.LargeNumericalEnum.ZERO)
    life_3 = models.CharField(max_length=32, choices=choices.LargeNumericalEnum.CHOICES, default=choices.LargeNumericalEnum.ZERO)
    movement_1 = models.CharField(max_length=32, choices=choices.NumericalEnum.CHOICES, default=choices.NumericalEnum.ZERO)
    movement_2 = models.CharField(max_length=32, choices=choices.NumericalEnum.CHOICES, default=choices.NumericalEnum.ZERO)
    movement_3 = models.CharField(max_length=32, choices=choices.NumericalEnum.CHOICES, default=choices.NumericalEnum.ZERO)
    melee_1 = models.CharField(max_length=32, choices=choices.DiceSuccessEnum.CHOICES, default=choices.DiceSuccessEnum.NONE)
    melee_2 = models.CharField(max_length=32, choices=choices.DiceSuccessEnum.CHOICES, default=choices.DiceSuccessEnum.NONE)
    melee_3 = models.CharField(max_length=32, choices=choices.DiceSuccessEnum.CHOICES, default=choices.DiceSuccessEnum.NONE)
    range_1 = models.CharField(max_length=32, choices=choices.DiceSuccessEnum.CHOICES, default=choices.DiceSuccessEnum.NONE)
    range_2 = models.CharField(max_length=32, choices=choices.DiceSuccessEnum.CHOICES, default=choices.DiceSuccessEnum.NONE)
    range_3 = models.CharField(max_length=32, choices=choices.DiceSuccessEnum.CHOICES, default=choices.DiceSuccessEnum.NONE)
    attacks_1 = models.CharField(max_length=32, choices=choices.NumericalDiceEnum.CHOICES, default=choices.NumericalDiceEnum.ZERO)
    attacks_2 = models.CharField(max_length=32, choices=choices.NumericalDiceEnum.CHOICES, default=choices.NumericalDiceEnum.ZERO)
    attacks_3 = models.CharField(max_length=32, choices=choices.NumericalDiceEnum.CHOICES, default=choices.NumericalDiceEnum.ZERO)


class Profile(models.Model):
    name = models.CharField(max_length=64)
    movement = models.CharField(max_length=32, choices=choices.DegressiveNumericalEnum.CHOICES, default=choices.DegressiveNumericalEnum.ZERO)
    melee = models.CharField(max_length=32, choices=choices.DegressiveDiceSuccessEnum.CHOICES, default=choices.DegressiveDiceSuccessEnum.NONE)
    range = models.CharField(max_length=32, choices=choices.DegressiveDiceSuccessEnum.CHOICES, default=choices.DegressiveDiceSuccessEnum.NONE)
    strength = models.CharField(max_length=32, choices=choices.NumericalEnum.CHOICES, default=choices.NumericalEnum.ZERO)
    toughness = models.CharField(max_length=32, choices=choices.NumericalEnum.CHOICES, default=choices.NumericalEnum.ZERO)
    life = models.CharField(max_length=32, choices=choices.DegressiveLargeNumericalEnum.CHOICES, default=choices.DegressiveLargeNumericalEnum.ZERO)
    attacks = models.CharField(max_length=32, choices=choices.DegressiveNumericalDiceEnum.CHOICES, default=choices.DegressiveNumericalDiceEnum.ZERO)
    command = models.CharField(max_length=32, choices=choices.NumericalEnum.CHOICES, default=choices.NumericalEnum.ZERO)
    armor = models.CharField(max_length=32, choices=choices.DiceSuccessEnum.CHOICES, default=choices.DiceSuccessEnum.NONE)
    invulnerability = models.CharField(max_length=32, choices=choices.DiceSuccessEnum.CHOICES, default=choices.DiceSuccessEnum.NONE)

    points = models.SmallIntegerField(default=1, validators=[MinValueValidator(1)])
    unit = models.ForeignKey(Unit, null=True, related_name='profiles')
    degressive = models.ForeignKey(DegressiveProfile, null=True, related_name='base_profiles')
    
    def __str__(self):
        return self.name
