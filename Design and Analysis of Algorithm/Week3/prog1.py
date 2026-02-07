# Write a code for max-min algorithm with calculating time complexity

def max_min(arr, low, high):
    # Only for one element
    if low == high:
        return arr[low], arr[low]
    
    # Only for two element 
    if high == low + 1:
        if arr[low] > arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]
        

    # General case
    mid = (low + high )//2
    max1, min1 = max_min(arr, low, mid)
    max2, min2 = max_min(arr, mid+1, high)

    return max(max1, max2), min(min1, min2)


arr = [9,6,2,4,10,12,8,13]
maximum, minimum = max_min(arr, 0, len(arr)-1)

print("Maximum: ",maximum)
print("Minimm: ",minimum)