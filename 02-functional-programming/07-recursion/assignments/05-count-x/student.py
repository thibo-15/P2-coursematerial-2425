def countX(text):
    if not text:
        return 0
    return (1 if text[0] == 'x' else 0) + countX(text[1:])

#print(countX("xxhixx"))  # Output: 4
#print(countX("hello"))   # Output: 0
#print(countX("XxXx"))    # Output: 2 (alleen kleine 'x' telt)