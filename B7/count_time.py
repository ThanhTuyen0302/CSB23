# tao nguyen lieu ngau nhien
import random
arr1 = random.sample(range(100), 10)
arr2 = random.sample(range(100), 10)

# dem so lan swap trong thuat toan Bubble
def bubble_sort(arr):
    # bien count
    swapped_count = 0
    print("Arr chua sort: ", arr)
    for i in range(len(arr)):
        swapped = False # bien kiem tra co thay doi khong   
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                # swap
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped_count += 1
                print(f"Lan swap {swapped_count:02}: {arr}")
                swapped = True
        if not swapped:
            break
# test
bubble_sort(arr1)
# --------------------------------
# dem so lan chen trong thuat toan Insertion
def insertion_sort(arr):
    # duyet qua tung phan tu -> tim vi tri nho nhat
    for index in range(1, len(arr)):
        insert_index = index       
        current_value = arr.pop(index) # xoa phan tu tai index
        print(arr, f"Cat phan tu {current_value}")
        for j in range(index - 1, -1, -1):
            if arr[j] > current_value:
                insert_index = j
        arr.insert(insert_index, current_value) # them lai phan tu vao vi tri moi 
        print(f"Lan chen {index:02}: {arr}")
    return arr
# test
arr2 = insertion_sort(arr2)
print("Arr da sort: ", arr2)
