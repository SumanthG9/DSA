# # this is achieved by storing the elements of an array in the reverse order in a temporay array and copying them back to the original array hence reversing the array
# Time Complexity: O(n), Copying elements to a new array is a linear operation.
# Auxiliary Space: O(n), as we are using an extra array to store the reversed array.
def revarr(arr):
    n = len(arr)
    temp = [0]*n
    for i in range(n):
        temp[i] = arr[n-1-i]

    for i in range(n):
        arr[i] = temp [i]

arr =[1,2,3,4,5]
revarr(arr)
print(arr)