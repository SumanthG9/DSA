# using a temporary array to sort the array and move the zeros to the end
# time complexity - O(n) space complexity - O(n)

def mvzeros(arr):
    n = len(arr)
    temp = [0]*n
    j = 0
    for i in range(n):
        if arr[i] != 0:
            temp[j] = arr[i]
            j = j + 1


    while j < n:
        temp[j] = 0
        j += 1

    for i in range(n):
        arr[i] = temp[i]

arr = [1,4,5,767,34,0,34,0,6676,7,0]
mvzeros(arr)
print(arr)
