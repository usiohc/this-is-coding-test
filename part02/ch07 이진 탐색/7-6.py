# 처음 시도

# def binary_search(array, target, start, end):
#     while start<=end:
#         mid = (start+end)//2
#         length = 0
#         for i in array:
#             if i > mid:
#                 length += i - mid
#         print(mid, length)
        
#         if length == target:
#             print(mid)
#             break
#         elif length < target:
#             end = mid-1
#         elif length > target:
#             start = mid+1
    
#     return


# 답안 예시 보고 다시
def binary_search(array, target, start, end):
    result = 0

    while start<=end:
        mid = (start+end)//2
        length = 0
        for i in array:
            if i > mid:
                length += i - mid
        
        if length < target:
            end = mid-1
        else:
            result = mid
            start = mid + 1

    print(result)
    return


n, m = map(int, input().split())
array = list(map(int, input().split()))

binary_search(array, m, 0, max(array))