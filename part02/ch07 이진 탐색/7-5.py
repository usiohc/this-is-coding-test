def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid

        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return False


n = int(input())
nNums = sorted(list(map(int, input().split())))

m = int(input())
mNums = sorted(list(map(int, input().split())))

for m in mNums:
    result = binary_search(nNums, m, 0, n-1)
    if result:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')