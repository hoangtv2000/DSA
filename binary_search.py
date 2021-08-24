def binary_search(sorted_list, item):
    # keep track of low and high index
    low = 0
    high = len(sorted_list) - 1

    while low <= high: # when we haven't narrowed down to one element
        mid = (low + high) // 2 # index of the middle element
        guess = sorted_list[mid] # value of the middle element

        if guess == item: 
            return mid
        elif guess > item: 
            # Guess is too high,
            # we narrow our search on the "left" part
            high = mid - 1
        else:
            # Guess is too low,
            # we narrow our search on the "right" part
            low = mid + 1

    # If we have anrrowed down to one element but still can not find the item
    # => Item is not in the list 
    return -1