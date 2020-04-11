from abc import ABC, abstractmethod
import random

class Unit(ABC):
    _name = None
    _strength = 0
    _health = 0
    _defence = 0
    _defence_coeff = 0
    _double_attack = 0

    def _check_name(self, name):
        if isinstance(name, str) and len(name) <= 15:
            return name

    def __init__(self, name, strength, health, defence):
        self._name = self._check_name(name)
        if type(strength) == type(defence) == int and strength > 0 and defence > 0:
            self._strength = strength
            self._defence = defence
        self.health = health

    def _check_double_attack(self):
        coeff_a = random.random()
        if self._double_attack >= coeff_a:
            return True

    def _check_defence(self, opponent):
        coeff_d = random.random()
        if opponent._defence_coeff >= coeff_d:
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

    def __str__(self):
        return f'Health - {self._health}.'


class Vampire(Unit):
    _vamp = "I\'m Vampire"
    _double_attack = 0.6
    _defence_coeff = 0.3

    def _attack(self, opponent):
        dmg = self._strength
        if self._check_double_attack():
            dmg = dmg * 2
        if self._check_defence(opponent):
            dmg -= opponent._defence
        opponent.health -= dmg
        self._health += round(dmg * 0.2)

    def __str__(self):
        return f'{self._vamp}. Health - {self._health}.'


class Knight(Unit):
    _knight = "I\'m Knight"
    _double_attack = 0.5
    _defence_coeff = 0.3

    def _attack(self, opponent):
        dmg = self._strength
        if self._check_double_attack():
            dmg = dmg * 2
        if self._check_defence(opponent):
            dmg -= opponent._defence
        opponent.health -= dmg * 1.2

    def __str__(self):
        return f'{self._knight}. Health - {self._health}.'


class Monk(Unit):
    _monk = "I\'m Monk"
    _double_attack = 0.6
    _defence_coeff = 0.3

    def _attack(self, opponent):
        dmg = self._strength
        if self._check_double_attack():
            dmg = dmg * 2
        if self._check_defence(opponent):
            dmg -= opponent._defence
        opponent.health -= dmg
        self._health = round(self._health * 1.1)

    def __str__(self):
        return f'{self._monk}. Health - {self._health}.'


class Rogue(Unit):
    _double_attack = 0.4
    _defence_coeff = 0.4
    _rogue = "I\'m Rogue"

    def _attack(self, opponent):
        dmg = self._strength
        if self._check_double_attack():
            dmg = dmg * 2
        if self._check_defence(opponent):
            dmg -= opponent._defence
        opponent.health -= dmg

    def __str__(self):
        return f'{self._rogue}. Health - {self._health}.'

class Dwarf(Unit):
    _dwarf = "I\'m Dwarf"
    _defence_coeff = 0.2
    _double_attack = 0.2

    def _attack(self, opponent):
        dmg = self._strength
        if self._check_double_attack:
            dmg = dmg * 2
        if self._check_defence(opponent):
            dmg -= opponent._defence
        opponent.health -= dmg

    def __str__(self):
        return f'{self._dwarf}. Health - {self._health}.'


k1 = Knight(name='Artur', strength=40, health=200, defence=15)
r1 = Rogue(name='Aragorn', strength=50, health=200, defence=20)
d1 = Dwarf(name='Gimli', strength=30, health=200, defence=15)
v1 = Vampire(name='Drakula', strength=40, health=200, defence=20)
m1 = Monk(name='Gendalf', strength=50, health=200, defence=15)

#print(r1)
# print(d1)
# print(k1)
# print(v1)
# print(m1)
#
# #print(r1._health)
# print(v1._health)
# r1.attack(v1)
# #print(r1._health)
# print(v1._health)
# r1.attack(v1)
# #print(r1._health)
# print(v1._health)
# r1.attack(v1)
# #print(r1._health)
# print(v1._health)
# r1.attack(v1)
# #print(r1._health)
# print(v1._health)


class Battle():
    _opponent1 = None
    _opponent2 = None
    _units = None

    def __init__(self, opp1, opp2):
        if isinstance(opp1, Unit) and isinstance(opp2, Unit):
            self._opponent1 = opp1
            self._opponent2 = opp2
            self._units = (self._opponent1, self._opponent2)

    def _attack_op1(self):
        self._opponent1._attack(self._opponent2)
        print(f'{self._opponent1.__class__.__name__} is attacking. Health {self._opponent2.__class__.__name__} - {self._opponent2._health}')

    def _attack_op2(self):
        self._opponent2._attack(self._opponent1)
        print(f'{self._opponent2.__class__.__name__} is attacking. Health {self._opponent1.__class__.__name__} - {self._opponent1._health}')

    def _battle(self):
        random_unit = random.choice(self._units)

        if random_unit == self._opponent1:
            while 1:
                self._attack_op1()
                if self._opponent2._health == 0:
                    return f'{self._opponent2.__class__.__name__} is dead.'

                self._attack_op2()
                if self._opponent1._health == 0:
                    return f'{self._opponent1.__class__.__name__} is dead.'

        else:
            while 1:
                self._attack_op2()
                if self._opponent1._health == 0:
                    return f'{self._opponent1.__class__.__name__} is dead.'

                self._attack_op1()
                return f'{self._opponent2.__class__.__name__} is dead.'


battle1 = Battle(k1, v1)
print(battle1._battle())
