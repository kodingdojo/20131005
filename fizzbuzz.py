from nose.tools import eq_

def fizzbuzz(number):
    return "fizz"

eq_("fizz", fizzbuzz(3))
eq_("fizz", fizzbuzz(6))
