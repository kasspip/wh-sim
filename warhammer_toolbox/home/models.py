from __future__ import unicode_literals

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from home.choices import Race


class Army(models.Model):
    name = models.CharField(max_length=64)
    icon = models.ImageField(upload_to='faction', null=True)
    race = models.CharField(choices=Race.CHOICES, default=Race.OTHER, max_length=32)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=64)
    icon = models.ImageField(upload_to='role', null=True)
    display_order = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.name


class Keyword(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Figurine(models.Model):

    name = models.CharField(max_length=64)
    picture = models.ImageField(upload_to='uploaded_images', null=True, blank=True)
    movement = models.SmallIntegerField(default=0, validators=[MinValueValidator(0)])
    melee = models.SmallIntegerField(default=6, validators=[MinValueValidator(0), MaxValueValidator(6)])
    range = models.SmallIntegerField(default=6, validators=[MinValueValidator(0), MaxValueValidator(6)])
    strength = models.SmallIntegerField(default=1, validators=[MinValueValidator(1)])
    toughness = models.SmallIntegerField(default=1, validators=[MinValueValidator(1)])
    life = models.SmallIntegerField(default=1, validators=[MinValueValidator(1)])
    attacks = models.SmallIntegerField(default=0, validators=[MinValueValidator(0)])
    armor = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(6)])
    command = models.SmallIntegerField(default=2, validators=[MinValueValidator(2), MaxValueValidator(12)])
    points = models.SmallIntegerField(default=1, validators=[MinValueValidator(1)])
    invulnerability = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(6)])
    army = models.ForeignKey(Army, related_name='figurines', null=True)
    # role = models.ForeignKey(Role, related_name='figurines', null=True)
    # keywords = models.ManyToManyField(Keyword, related_name='figurines')
    # category = models.ForeignKey(Category, related_name='figurines', null=True)

    def __str__(self):
        return self.name

    @staticmethod
    def _dice_display(value):
        if value == 0:
            return '-'
        else:
            return "%s +" % value

    def get_movement_display(self):
        return "%s ''" % self.movement

    def get_melee_display(self):
        return self._dice_display(self.melee)

    def get_range_display(self):
        return self._dice_display(self.range)

    def get_strength_display(self):
        return self.strength

    def get_toughness_display(self):
        return self.toughness

    def get_life_display(self):
        return self.life

    def get_attacks_display(self):
        return self.attacks

    def get_command_display(self):
        return self.command

    def get_armor_display(self):
        return self._dice_display(self.armor)

    def get_points_display(self):
        return "%s pts" % self.points

    def get_invulnerabilty_display(self):
        return self._dice_display(self.invulnerability)


class FigurineGroup(models.Model):
    figurine = models.ForeignKey(Figurine, null=True)
    count = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.figurine.name + " x " + str(self.count)


class Squad(models.Model):
    name = models.CharField(max_length=64)
    figurines = models.ManyToManyField(FigurineGroup, 'squads')
    power = models.SmallIntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name


class Weapon(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name