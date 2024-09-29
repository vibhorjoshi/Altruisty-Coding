from collections import deque

def max_of_minimums(arr, k):
    n = len(arr)
    
    # Deque to store indices of array elements
    dq = deque()
    
    # Result to store the maximum of minimums
    max_of_mins = float('-inf')
    
    # Iterate over all elements of the array
    for i in range(n):
        # Remove elements from the back of the deque if they are greater than the current element
        while dq and arr[dq[-1]] >= arr[i]:
            dq.pop()
        
        # Add the current element at the back of the deque
        dq.append(i)
        
        # Remove the elements which are out of this window
        if dq[0] <= i - k:
            dq.popleft()
        
        # Once we have processed the first 'k' elements, we can start recording results
        if i >= k - 1:
            # The element at the front of the deque is the minimum of the current window
            max_of_mins = max(max_of_mins, arr[dq[0]])
    
    return max_of_mins

# Custom Test Case
k = 1
arr = [1, 2, 3, 1, 2]

# Output the result for the custom test input
print(max_of_minimums(arr, k))  # Expected Output: 3
