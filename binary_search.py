def find(search_list, value):
    lowest = 0
    highest = len(search_list) - 1
    while lowest <= highest:
        middle = (highest - lowest) // 2
        if search_list[middle] == value:
            return search_list.index(search_list[middle])
        elif search_list[middle] > value:
            highest -= search_list.index(search_list[middle])
        elif search_list[lowest] < value:
            lowset += search_list.index(search_list[middle])
        
    raise ValueError("value not in array")