def binary_search_iterative(arr,k):
    low = 0
    high = len(arr)-1
    mid = 0
    
    while low <= high:
        mid = (low + high)//2
        if arr[mid] < k:
            low = mid + 1
        elif arr[mid] > k:
            high = mid - 1
        else:
            return mid
    return -1


nums = [1,2,3,4,5,6,7,8,9]
(binary_search_iterative(nums,7))