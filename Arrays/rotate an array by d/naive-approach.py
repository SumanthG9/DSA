# # In each iteration, shift the elements by one position to the left in a circular fashion (the first element becomes the last). Perform this operation d times to rotate the elements to the left by d position

#  Let us take arr[] = {1, 2, 3, 4, 5, 6}, d = 2.

# First Step:
#         => Rotate to left by one position.
#         => arr[] = {2, 3, 4, 5, 6, 1}
# Second Step:
#         => Rotate again to left by one position
#         => arr[] = {3, 4, 5, 6, 1, 2}
# Rotation is done 2 times.
# So the array becomes arr[] = {3, 4, 5, 6, 1, 2}

def rotatetoleftbyd(arr,d):
    n = len(arr)
    d = int(d)
    for i in range(d):
        arr[i], arr[n-i-1] = arr[n-1-i], arr[i]

arr =[1,2,3,4,5]
rotatetoleftbyd(arr,4)
print(arr)