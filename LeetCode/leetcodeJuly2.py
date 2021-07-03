def findKClosestElements(arr, k, x):
    left = 0
    right = len(arr) - 1
    while right - left >= k:
        if abs(arr[left] - x) > abs(arr[right] - x):
            left = left + 1
        else:
            right = right - 1
    return arr[left:left + k]
 
if __name__ == '__main__':
    arr = [1,2,3,4,5]
    x = -1
    k = 4
 
    print(findKClosestElements(arr, k, x))