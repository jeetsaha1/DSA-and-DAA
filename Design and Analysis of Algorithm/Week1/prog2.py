# 2. Perform binary search on the array: {12, 13, 18, 20, 23} with key = 14.


def binary_search(arr,key):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if key < arr[mid]:
            high = mid -1
        elif key > arr[mid]:
            low = mid+1
        else:
            return mid
    return -1


arr = [12, 13, 18, 20, 23]
key = 15

res = binary_search(arr,key)

if(res != -1):
    print("The element is found")
else:
    print("The element is not found")




# Algorithm:

# FUNCTION binary_search(Arr,n,target)
# BEGIN
#     low <- 0                          
#     high <- n-1
#     WHILE low <= high DO
#         mid <- (low+high)//2
#         IF key < arr[mid] THEN
#             high = mid -1
#         ELSE IF key > arr[mid] THEN
#             low = mid+1
#         ELSE
#             RETURN mid
#     END WHILE
#     RETURN -1
# END




# Time Complexity:
# n → n/2 → n/4 → n/8 → … → 1
# T(n) = n/(2^k)
# Now,  n/(2^k) = 1
# =>  log n = k log 2
# =>  k = log n (base 2)
  
# T(n) ~= O(log n)
