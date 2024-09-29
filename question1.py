  min_price = float('inf')  # Set initial min_price to infinity
    max_profit = 0            # Set initial max_profit to 0
    
    # Loop through each price
    for price in prices:
        # Update the minimum price seen so far
        if price < min_price:
            min_price = price
        # Calculate the current profit if sold at today's price
        profit = price - min_price
        # Update the maximum profit seen so far
        if profit > max_profit:
            max_profit = profit
    
    return max_profit

# Custom Test Input
n = 7
prices = [1, 9, 2, 11, 1, 9, 2]

# Output the result for the custom test input
print(max_profit(prices))  # Expected Output: 10
