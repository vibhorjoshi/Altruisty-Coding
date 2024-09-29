def find_odd_balloon(n, balloons):
    # Step 1: Create a dictionary to store frequencies of each balloon color
    freq = {}
    
    # Count the frequency of each balloon
    for balloon in balloons:
        if balloon in freq:
            freq[balloon] += 1
        else:
            freq[balloon] = 1
    
    # Step 2: Find the first balloon with an odd frequency
    for balloon in balloons:
        if freq[balloon] % 2 != 0:
            return balloon
    
    # Step 3: If all balloons have even counts
    return "All are even"

# Custom Test Case Input
n = 7  # Number of balloons
balloons = ['r', 'g', 'b', 'b', 'g', 'y', 'y']

# Call the function and print the result
result = find_odd_balloon(n, balloons)
print(result)  # Expected Output: r
