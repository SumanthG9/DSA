# time complexity - O(n) space complexity - O(1)
def mvzeros(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i],arr[count] = arr[count],arr[i]
            count += 1

arr = [1,4,5,767,34,0,34,0,6676,7,0]
mvzeros(arr)
print(arr)