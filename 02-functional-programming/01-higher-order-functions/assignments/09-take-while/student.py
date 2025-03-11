def take_while(xs, condition):
    first_lst = []
    second_lst = []

    for x in xs:
        if condition(x):
            first_lst.append(x)
        else:
            second_lst.extend(xs[len(first_lst) : ])
            break

    return (first_lst, second_lst)


def is_negative(x):
    return x < 0

# Test the function
result = take_while([-4, -2, 0, -1, 4, 6], is_negative)
print(result)