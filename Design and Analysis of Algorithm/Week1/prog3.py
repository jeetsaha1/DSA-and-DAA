# 3. Perform insertion sort, selection sort and bubble sort on the following unsorted array:  {28, 12, 15, 13, 25} 

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i-1
        temp = arr[i]

        while j>= 0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j-= 1
        arr[j+1] = temp

# Algorithm:
# FUNCTION insertion_sort(arr,n)
# BEGIN
#     FOR i =1 TO n-1:                          n+1
#         j <- i-1                              1
#         temp <- arr[i]                        1
    
#         WHILE j>= 0 AND arr[j] > temp THEN    n*(n+1)/2
#             arr[j+1] <- arr[j]                n*n
#             j<- j - 1                         n*n
#         END WHILE     
#         arr[j+1] <- temp                      n
#     END FOR
# END


# Time Complexity:
# T(n) = n + (1 + 2 + … + n)
#      = n + n(n+1)/2
#      = (n² + 3n)/2
#      ≈ O(n²)


def selction_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        if min != i:
            arr[min], arr[i] = arr[i], arr[min]



# Algorithm:
# FUNCTION selction_sort(arr,n)
# BEGIN
#     FOR i = 0 TO n-1 DO                               
#         min <- i                                      
#         FOR j = i+1 TO n-1 DO                         n*(n-1)/2
#             IF arr[min] > arr[j] THEN                 
#                 min <- j
#             END IF
#         IF min != i THEN                              
#             arr[min], arr[i] <- arr[i], arr[min]
#         END IF
#     END FOR
# END


# Time Complexity:

# T(n) = (n−1) + (n−2) + … + 1
#      = n(n−1) / 2
#     O(n^2)

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1] , arr[j]

# Algorithm:
# FUNCTION bubble_sort(arr,n):
#     FOR i = 0 TO n-1 DO
#         FOR j = 0 TO n-i-1 DO
#             IF arr[j] > arr[j+1] THEN
#                 arr[j], arr[j+1] <=  arr[j+1] , arr[j]
#             END IF
#         END FOR
#     END FOR
# END

# Time Complexity:

# T(n) = (n−1) + (n−2) + … + 1
#      = n(n−1) / 2
#     O(n^2)

arr = [28, 12, 15, 13, 25]
bubble_sort(arr)
print(arr)