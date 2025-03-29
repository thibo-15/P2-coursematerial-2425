def findMaximum(list):
    if not list:
        raise IndexError("Connot find max of an ampty list")
    if len(list) == 1:
        return list[0]
    max_rest = findMaximum(list[1:])
    return max(list[0], max_rest)

#numbers = [3, 1, 9, 7, 2]
#print(findMaximum(numbers))  # Output: 9