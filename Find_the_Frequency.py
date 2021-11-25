def findFrequency (arr, n, x):
    # Your Code Here
    counter = 0
    for i in range(n):
        if arr[i] == x:
            counter += 1
    return counter
