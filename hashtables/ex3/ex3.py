def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []
    #Loop through data
    for array in arrays:
        # Retreive inner array value
        for item in array:
            if item in cache:
                #If the item is found in the cache then increment the value by one
                cache[item] += 1
            else:
                # If it is not found, set the value to one
                cache[item] = 1

    for key, value in cache.items():
        # For each value in the cache, if the value is equal to the amount of inner arrays then append the result to the array
        if value == len(arrays):
            result.append(key)
    return result


    


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))