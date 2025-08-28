#Time Complexity - O(n) Space complexity-O(1)

def secondlargest(arr):
    n = len(arr)
    largest = -1
    second_largest = -1
    for i in range(n):
        if arr[i] >= largest:
            second_largest = largest
            largest = arr[i]
            
        elif arr[i] >= second_largest and arr[i] != largest:
            second_largest = arr[i]
    return second_largest


arr = [12,45,67,89,10]
print(secondlargest(arr))
        