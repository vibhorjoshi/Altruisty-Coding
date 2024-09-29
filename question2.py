def count_frogs(s, start_indices, end_indices):
    n = len(s)
    
    # Prefix sum array to count number of '*' encountered up to each index
    star_prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        star_prefix[i] = star_prefix[i - 1] + (1 if s[i - 1] == '*' else 0)
    
    # Left boundary array to find the nearest '|' to the left of each index
    left_boundary = [-1] * (n + 1)
    last_pipe = -1
    for i in range(1, n + 1):
        if s[i - 1] == '|':
            last_pipe = i
        left_boundary[i] = last_pipe
    
    # Right boundary array to find the nearest '|' to the right of each index
    right_boundary = [-1] * (n + 1)
    last_pipe = -1
    for i in range(n, 0, -1):
        if s[i - 1] == '|':
            last_pipe = i
        right_boundary[i] = last_pipe
    
    results = []
    
    # For each pair of start and end indices, calculate the number of '*' between '|'
    for start, end in zip(start_indices, end_indices):
        # Find the first valid '|' within the range
        left = right_boundary[start]
        right = left_boundary[end]
        
        if left != -1 and right != -1 and left < right:
            results.append(star_prefix[right] - star_prefix[left])
        else:
            results.append(0)
    
    return results

# Custom Test Case 0
s = "*|*|"
start_indices = [1]
end_indices = [3]

# Output the result for the custom test input
print(count_frogs(s, start_indices, end_indices))  # Expected Output: [0]

