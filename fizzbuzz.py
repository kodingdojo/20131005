from nose.tools import eq_


def fizzbuzz(number):
    if number == 0:
        return "invalid number!"

    if number % 15 == 0:
        return "fizzbuzz"

    if number % 3 == 0:
        return "fizz"

    elif number % 5 == 0:
        return "buzz"

    else:
        return str(number)


eq_("invalid number!", fizzbuzz(0))

eq_("fizz", fizzbuzz(3))
eq_("fizz", fizzbuzz(6))

eq_("buzz", fizzbuzz(5))
eq_("buzz", fizzbuzz(10))

eq_("fizzbuzz", fizzbuzz(15))
eq_("fizzbuzz", fizzbuzz(45))

eq_("2", fizzbuzz(2))
eq_("1", fizzbuzz(1))
