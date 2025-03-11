def find(lst, condition):
    for item in lst:
        if condition(item):
            return item
    return None

def has_consecutive_characters(string):
    for index in range(len(string) - 1):
        if string[index] == string[index + 1]:
            return True
    return False

def find_string_with_consecutive_characters(string):
    return find(string, has_consecutive_characters)

print(find(["monkey", "banana", "computer", "yellow", "oddish"], has_consecutive_characters))  # "yellow"
