from __future__ import unicode_literals

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from home.choices import DiceRequirement


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


class Profile(models.Model):
    name = models.CharField(max_length=64)
    movement = models.SmallIntegerField(default=0, validators=[MinValueValidator(0)])
    melee = models.CharField(max_length=32, choices=DiceRequirement.CHOICES, default=DiceRequirement.NONE)
    range = models.CharField(max_length=32, choices=DiceRequirement.CHOICES, default=DiceRequirement.NONE)
    strength = models.SmallIntegerField(default=1, validators=[MinValueValidator(1)])
    toughness = models.SmallIntegerField(default=1, validators=[MinValueValidator(1)])
    life = models.SmallIntegerField(default=1, validators=[MinValueValidator(1)])
    attacks = models.SmallIntegerField(default=0, validators=[MinValueValidator(0)])
    command = models.SmallIntegerField(default=2, validators=[MinValueValidator(2), MaxValueValidator(12)])
    armor = models.CharField(max_length=32, choices=DiceRequirement.CHOICES, default=DiceRequirement.NONE)
    invulnerability = models.CharField(max_length=32, choices=DiceRequirement.CHOICES, default=DiceRequirement.NONE)

    points = models.SmallIntegerField(default=1, validators=[MinValueValidator(1)])
    unit = models.ForeignKey(Unit, null=True, related_name='profiles')

    def __str__(self):
        return self.name




