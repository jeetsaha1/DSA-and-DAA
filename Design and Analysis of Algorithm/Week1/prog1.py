# 1. Perform linear search on the array: {5, 7, 13,15,17} with key = 13. 

def linear_search(arr,target):
    for i in range(len(arr)):
        if(arr[i] == target):
            return i
    return -1

arr = [5,7,13,15,17]
key = 13

res = linear_search(arr,key)
if(res != -1):
    print("The element is found at",res,"index")
else:
    print("The element is not found ")



# Algorithm:

# FUNCTION linear_search(Arr,n,target)
# BEGIN
#     FOR i = 0 TO n-1 DO                   (n+1)
#         IF Arr[i] = target THEN           n
#             RETURN True                   1
#         END IF
#     END FOR
#     RETURN False                          1
# END




# Time Complexity:

# T(n) = (n+1) + n + 2
#      = 2n + 3
# T(n) ~= O(n)