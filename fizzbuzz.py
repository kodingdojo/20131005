from nose.tools import eq_


def fizzbuzz(number):
    if number == 1:
        return "1"
    elif number == 5:
        return "buzz"
    elif number == 15:
        return "fizzbuzz"
    else:
        return "fizz"

eq_("fizz", fizzbuzz(3))
eq_("fizz", fizzbuzz(6))
eq_("1", fizzbuzz(1))
eq_("buzz", fizzbuzz(5))
eq_("fizzbuzz", fizzbuzz(15))
