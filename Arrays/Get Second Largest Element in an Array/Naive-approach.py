#Naive approach is done using sorting
#Time complexity -O(n*logn) for using sort  & Space Complexity - o(1)

def secondlargest(arr):

    n =len(arr)
    arr.sort()
    for i in range(n-2,-1,-1):
        if arr[i]!= arr[n-1]:
            return arr[i]      
    return -1

arr = [12,45,67,89,10]
print(secondlargest(arr))