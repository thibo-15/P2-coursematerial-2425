def indices_of(xs, condition):
    indices = []
    for index, item in enumerate(xs):
        if condition(item):
            indices.append(index)
    return indices

def is_palindrome(s):
    return s == s[::-1]

#result = indices_of(["kayak", "never", "rotator", "palindrome"], is_palindrome)
#print(result)