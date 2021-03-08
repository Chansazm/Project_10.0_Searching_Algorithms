def binary_search(nums,k):
    low = 0
    high = len(nums)-1
    mid = int(low+high//2)
    while low <= high:
        if nums[mid] == k:
            return mid
        elif k > nums[mid]:
            left = low + 1
        else:
            right = high - 1
        return k
    if low > high:
        return False



items = [1,2,3,4,5,6,7,8,9]
print(binary_search(items,3))