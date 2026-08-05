def find(search_list, value):
    lowest = 0
    # Grabs the length of the values in the search list and takes 1 to 
    # prevent reference from going out of range.
    highest = len(search_list) - 1

    # Scans through list until it is less than 0
    while lowest <= highest:
        # Finds median/middle of list.
        middle = (highest + lowest) // 2

        # If the number being looked at is the value, return the index of the number.
        if search_list[middle] == value:
            return search_list.index(search_list[middle])
        # If the looked at number is more than the value, reduce the max scope by reducing max parameter.
        elif search_list[middle] > value:
            highest = middle - 1
        # If the looked at number is less than the value, reduce the max scope by increasing min parameter.
        elif search_list[lowest] < value:
            lowest = middle + 1
        
    raise ValueError("value not in array")