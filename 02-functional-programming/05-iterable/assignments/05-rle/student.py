def rle_encode(data):
    iterator = iter(data) 
    try:
        current_char = next(iterator)  
        count = 1

        for char in iterator:
            if char == current_char:
                count += 1  
            else:
                yield (current_char, count)  
                current_char = char  
                count = 1

        yield (current_char, count)  

    except StopIteration:
        pass
