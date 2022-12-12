from math import gcd
from fractions import Fraction

import bottom as bottom
import top as top


# 1
def get_num(self):
    return self.num


def get_den(self):
    return self.den


# 2
def __add__(self, other):
    new_num = (self.num * other.den) + (self.den * other.num)
    new_den = self.den * other.den
    return (new_num, new_den)


#3
def __sub__(self, other, num, den):
    new_num = (self.num * other.den) * (self.den * other.num)
    new_den = self.den * other.den
    common = gcd(abs(num), abs(den))
    return (num//common, den//common)


def __mul__(self, other):

    num = self.num * other.num
    den = self.den * other.den
    return (num, den)


def __truediv__(self, other):
    num = self.num * other.den
    den = self.den * other.num
    common = gcd(abs(num), abs(den))
    return (num//common, den//common)

#4
def __gt__(self, other):
    first_num = self.num * other.den
    second_num = self.den * other.num
    return first_num > second_num


def __ge__(self, other):
    first_num = self.num * other.den
    second_num = self.den * other.num
    return first_num >= second_num


def __lt__(self, other):
    first_num = self.num * other.den
    second_num = self.den * other.num
    return first_num < second_num


def __le__(self, other):
    first_num = self.num * other.den
    second_num = self.den * other.num
    return first_num <= second_num


def __ne__(self, other):
    first_num = self.num * other.den
    second_num = self.den * other.num
    return first_num != second_num


#5
def __init__(top, bottom):
    if not isinstance(top, int):
        valErr = ValueError('{} is not an integer'.format(top))
        raise valErr
    if not isinstance(bottom, int):
        valErr = ValueError("{} is not an integer".format(bottom))
        raise valErr


#6
if top < 0 and bottom <0:
    top = abs(top)
    bottom = abs(bottom)
elif bottom < 0:
    top = -top
    bottom = abs(bottom)


#7
def __radd__(self, other):
    if other == 0:
        return self
    else:
        other = Fraction(other, 1)
        return self.__add_(other)


#8
def __iadd__(self, other):
    if isinstance(other, int):
        other = Fraction(other, 1)
    return self.__add__(other)


#9
def __repr__(self):
    return '%s(%r)' % (self.__class__, self.__str__())


def show(self):
    print(self.num, "/", self.den)

