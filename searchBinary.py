def search_binary(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        quick = list[mid]
        if quick == item:
            return mid
        if quick > item:
            high = mid-1
        else:
            low = mid + 1
    return

my_list = [1,2,3,4,5,6,7,8,9,0]
# my_list = [1,3,5,7,9]

print(search_binary(my_list, 1))