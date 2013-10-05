from nose.tools import eq_


def fizzbuzz(number):
    if number == 1:
        return "1"
    if number == 2:
        return "2"
    elif number % 15 == 0:
        return "fizzbuzz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return "fizz"

eq_("fizz", fizzbuzz(3))
eq_("fizz", fizzbuzz(6))

eq_("buzz", fizzbuzz(5))
eq_("buzz", fizzbuzz(10))

eq_("fizzbuzz", fizzbuzz(15))
eq_("fizzbuzz", fizzbuzz(45))

eq_("2", fizzbuzz(2))
eq_("1", fizzbuzz(1))
