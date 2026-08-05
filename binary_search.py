def find(search_list, value):
    lowest = 0
    highest = len(search_list - 1)
    while lowest <= highest:
        middle = search_list[highest - lowest]
        if middle == value:
            return middle
        elif middle > value:
            search_list[middle:].pop
        elif search_list < value:
            search_list[:middle].pop
    raise ValueError("value not in array")