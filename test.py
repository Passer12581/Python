def feb():
    fib = []
    a, b = 1, 1
    while len(fib) <= 19:
        a, b = a, a+b
        fib.append(a)    
    return fib
def biny_search(list_num, num):
    left = 0
    right = len(list_num) -1
    while left <= right:
        mid = (right + left) // 2
        if num < list_num[mid]:
            right = mid -1
        elif num > list_num[mid]:
            left = mid + 1
        else: return mid

    return 0



