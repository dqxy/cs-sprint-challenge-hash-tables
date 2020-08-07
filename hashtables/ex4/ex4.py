def has_negatives(a):
    """
    YOUR CODE HERE
    """
    cach = {}
    result = []
    #Set up the hash table
    for i in a:
        cach[i] = i
        #Check to see if its non-zero and negaive
        if i != 0 and -i in cach:
            # print(i)
            #Return the absolute value
            #Append item to the result list
            result.append((abs(i)))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))