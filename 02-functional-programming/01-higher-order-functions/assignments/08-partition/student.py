def partition(lst, condition):
    first_lst = []
    second_lst = []

    for item in lst:
        if condition(item):
            first_lst.append(item)
        else:
            second_lst.append(item)

    return (first_lst, second_lst)

def children_and_adults(people):
    def is_child(person):
        return person.age < 18
    
    children, adults = partition(people, is_child)
    return (children, adults)
