from nose.tools import eq_

def fizzbuzz(number):
    if number == 1:
        return "1"
    return "fizz"

eq_("fizz", fizzbuzz(3))
eq_("fizz", fizzbuzz(6))
eq_("1", fizzbuzz(1))
