def find(search_list, value):
    lowest = 0
    highest = len(search_list) - 1
    while lowest <= highest:
        middle = highest - lowest
        if search_list[middle] == value:
            return search_list.index(search_list[middle])
        
        
    raise ValueError("value not in array")