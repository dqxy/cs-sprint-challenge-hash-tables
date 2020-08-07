# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    f_cache = {}
    output = []

    # Loop through directory list
    for a in files:
        #Split the path after the slash "/" to isolate file name
        file = a.split('/')[-1]
     #   print ("asfafs",file)
        #Add the directory to the file cache
        if file in f_cache:
            f_cache[file].append(a)
        else:
            f_cache[file] = [a]
    #Check if the files cache contains the query
    for b in queries:
        #Checking the query in the cached files
        if b in f_cache:
            #If the file is in the directory list
            outputs = f_cache[b]
            #A is the path in the query
            for a in outputs:
                #Add the result to the path of the final output
                output.append(a)

    return output


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))