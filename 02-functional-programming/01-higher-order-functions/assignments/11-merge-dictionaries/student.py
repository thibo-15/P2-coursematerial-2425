def merge_dictionaries(d1, d2, merge_function):
    merged = {}
    
    all_keys = set(d1.keys()).union(d2.keys())
    
    for key in all_keys:
        if key in d1 and key in d2:
            merged[key] = merge_function(d1[key], d2[key])
        elif key in d1:
            merged[key] = d1[key]
        else:
            merged[key] = d2[key]
    
    return merged