def fizzbuzz():
    num = 1
    while True:
        if num % 3 == 0 and num % 5 == 0:
            yield 'fizzbuzz'
        elif num % 3 == 0:
                yield 'fizz'
        elif num % 5 == 0:
             yield 'buzz'
        else:
             yield str(num)
        num += 1
        