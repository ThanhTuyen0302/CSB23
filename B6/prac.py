def binary_search_loop(arr, target):
    #danh sach rong
    if not arr: return -1
    # tao mid, start, end
    start, end = 0, len(arr) - 1
    mid = (end - start) // 2 + start
    
    # lap tu start den end
    while start <= end:
        # =
        if arr[mid] == target:
            return mid
        # <
        if arr[mid] < target:
            start = mid + 1
        # >
        else:
            end = mid - 1
        # cap nhat mid
        mid = (end - start) // 2 + start
    # ket thuc vong while -> k tim thay
    return -1

try:
    n = int(input())
    if n <= 0:
        raise ValueError("N must be a positive integer")
    arr = input().split(" ")
    if len(arr) != n:
        raise ValueError("The number of elements does not match N")
    # yeu cau danh sach so int
    arr = [int(x) for x in arr]
    target = int(input())
    
    # thuc thi thuat toan
    result = binary_search_loop(arr, target)
    print(result)
except Exception as e:
    print("Error:", e)
finally:
    print("End.")