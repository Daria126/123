from abc import ABC, abstractmethod
import random

class Unit(ABC):
    _name = None
    _strength = 0
    _health = 0
    _double_attack = 0

    def _check_name(self, name):
        if isinstance(name, str) and len(name) <= 15:
            return name

    def __init__(self, name, strength, health):
        self._name = self._check_name(name)
        if isinstance(strength, int) and strength > 0:
            self._strength = strength
        self.health = health

    def _check_double_attack(self):
        coeff = random.random()
        if self._double_attack >= coeff:
            return True

    @abstractmethod
    def _attack(self, opponent):
        pass

    def attack(self, opponent):
        if not isinstance(opponent, Unit):
            raise Exception
        if opponent._health == 0:
            raise Exception(f'Opponent is dead.')

        if isinstance(opponent, Rogue):
            r_avoid = random.randint(1, 10)
            if r_avoid == 1:
                opponent.health = opponent.health
            else:
                return self._attack(opponent)
        else:
            return self._attack(opponent)

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, val):
        if not isinstance(val, (int, float)):
            raise Exception
        self._health = val if val > 0 else 0


class Vampire(Unit):
    _vamp = "I\'m Vampire"
    _double_attack = 0.6

    def _attack(self, opponent):
        dmg = self._strength
        if self._check_double_attack():
            dmg = dmg * 2
        opponent.health -= dmg
        self._health += dmg * 0.1

    # @property
    # def health(self):
    #     return self._health
    #
    # @health.setter
    # def health(self, val):
    #     if not isinstance(val, (int, float)):
    #         raise Exception
    #     self._health = val if val >= -50 else 0


class Knight(Unit):
    _knight = "I\'m Knight"
    _double_attack = 0.5

    def _attack(self, opponent):
        dmg = self._strength
        if self._check_double_attack():
            dmg = dmg * 2
        opponent.health -= dmg * 1.2


class Monk(Unit):
    _monk = "I\'m Monk"
    _double_attack = 0.6

    def _attack(self, opponent):
        dmg = self._strength
        if self._check_double_attack():
            dmg = dmg * 2
        opponent.health -= dmg
        self._health = round(self._health * 1.1)


class Rogue(Unit):
    _double_attack = 0.4
    _rogue = "I\'m Rogue"

    def _attack(self, opponent):
        dmg = self._strength
        if self._check_double_attack():
            dmg = dmg * 2
        opponent.health -= dmg


k1 = Knight(name='Artur', strength=40, health=200)
r1 = Rogue(name='Aragorn', strength=50, health=200)
d1 = Dwarf(name='Gimli', strength=30, health=200)
v1 = Vampire(name='Drakula', strength=40, health=200)
m1 = Monk(name='Gendalf', strength=50, health=200)

#print(r1._health)
print(v1._health)
r1.attack(v1)
#print(r1._health)
print(v1._health)
r1.attack(v1)
#print(r1._health)
print(v1._health)
r1.attack(v1)
#print(r1._health)
print(v1._health)
r1.attack(v1)
#print(r1._health)
print(v1._health)
r1.attack(v1)
#print(r1._health)
print(v1._health)
r1.attack(v1)
#print(r1._health)
print(v1._health)