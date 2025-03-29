def sum_numbers(number):
    if number < 0:
        number = -number

    if number < 10:
        return number
    return number % 10 + sum_numbers(number // 10)

#print(sum_numbers(234))
#print(sum_numbers(-153))
          