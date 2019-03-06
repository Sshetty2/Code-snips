def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low+high)
        guess = arr[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None



def binary_search_squared(n):
    low = 0
    high = n
    mid = (low+high)*.5
    while low <= high:
        guess = mid
        if mid*mid == n:
            print("found num")
            return mid
        if mid*mid > n:
		
            high = mid
        else:
            low = mid
        mid = (low+high)*.5
    return None



