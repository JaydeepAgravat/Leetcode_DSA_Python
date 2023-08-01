# Q.1 Maximum and minimum of an array using minimum number of comparisons

# Time Complexity : O(n)
# Space Complexity : O(1)
# Number of Comparisons :
  #  If n is odd  : 3*(n-1)/2     
  #  If n is even : 3n/2 - 2

def find_max_min(arr):
    n = len(arr)
    
    if n==1:
        return arr[0], arr[0]
    elif n%2==0:
        mx = max(arr[0], arr[1])
        mn = min(arr[0], arr[1])
        i = 2
    else:
        mx = mn = arr[0]
        i = 1
    
    while (i<=n-2):
        if arr[i] < arr[i+1]:
            mx = max(mx, arr[i+1])
            mn = min(mn, arr[i])
        else:
            mx = max(mx, arr[i])
            mn = min(mn, arr[i+1])
        i += 2
    
    return mx, mn
  
# Q.2 Write a program to reverse an array or string

# Time Complexity : O(n)
# Space Complexity : O(1)

def rev(arr):
    low = 0
    high = len(arr)-1
    while low<=high:
        arr[low], arr[high] = arr[high], arr[low]
        low += 1
        high -= 1
    return arr
