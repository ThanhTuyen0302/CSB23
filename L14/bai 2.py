def majority_element(nums):
    if not nums:
        return []

    # Có tối đa 2 phần tử xuất hiện > n/3 lần
    candidate1 = candidate2 = None
    count1 = count2 = 0

    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1 = num
            count1 = 1
        elif count2 == 0:
            candidate2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1

    # Kiểm tra lại số lần xuất hiện
    result = []
    n = len(nums)
    for c in [candidate1, candidate2]:
        if c is not None and nums.count(c) > n // 3 and c not in result:
            result.append(c)
    return result