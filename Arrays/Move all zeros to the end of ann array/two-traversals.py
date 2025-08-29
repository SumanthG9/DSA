# time complexity - O(n) space complexity - O(1)

def mvzeros(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count = count + 1
    while count < len(arr):
        arr[count] = 0
        count += 1

arr = [1,4,5,767,34,0,34,0,6676,7,0]
mvzeros(arr)
print(arr)
