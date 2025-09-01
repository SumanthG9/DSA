# [Expected Approach - 2] By Swapping Elements - O(n) Time and O(1) Space
# The idea is to iterate over the first half of the array and swap each element with its corresponding element from the end. So, while iterating over the first half, any element at index i is swapped with the element at index (n - i - 1).

def revarr(arr):
    n = len(arr)
    for i in range(n//2):
        arr[i],arr[n-i-1] = arr[n-1-i],arr[i]

arr =[1,2,3,4,5]
revarr(arr)
print(arr)