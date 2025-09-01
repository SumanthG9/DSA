# [Expected Approach - 1] Using Two Pointers - O(n) Time and O(1) Space
# The idea is to maintain two pointers: left and right, such that left points at the beginning of the array and right points to the end of the array. 

# While left pointer is less than the right pointer, swap the elements at these two positions. After each swap, increment the left pointer and decrement the right pointer to move towards the center of array. This will swap all the elements in the first half with their corresponding element in the second half.

def revarr(arr):
    n = len(arr)
    left = 0
    right = n-1
    while left < right:
        arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -= 1

arr =[1,2,3,4,5]
revarr(arr)
print(arr)