def find_fittest_trainees(oxygen_levels):
    # Check if all oxygen levels are in the valid range (1-100)
    if any(level < 1 or level > 100 for level in oxygen_levels):
        return "INVALID INPUT"
    
    # Step 2: Initialize variables for each trainee's total oxygen
    trainees = [0, 0, 0]
    
    # Sum the oxygen levels for each trainee across the 3 rounds
    for i in range(3):
        trainees[0] += oxygen_levels[i * 3]     # Trainee 1
        trainees[1] += oxygen_levels[i * 3 + 1] # Trainee 2
        trainees[2] += oxygen_levels[i * 3 + 2] # Trainee 3
    
    # Step 3: Calculate average oxygen levels for each trainee
    averages = [round(total / 3) for total in trainees]
    
    # Step 4: Find the maximum average oxygen level
    max_average = max(averages)
    
    # Step 5: Check if all trainees are unfit
    if max_average < 70:
        return "All trainees are unfit"
    
    # Step 6: Find trainees with the maximum average oxygen level
    fittest_trainees = [i + 1 for i, avg in enumerate(averages) if avg == max_average]
    
    # Step 7: Prepare the output in the desired format
    result = ""
    for trainee in fittest_trainees:
        result += f"Trainee Number : {trainee}\n"
    
    return result.strip()

# Example Test Case Input
oxygen_levels = [
    95, 92, 95,  # Round 1
    92, 90, 92,  # Round 2
    90, 92, 90   # Round 3
]

# Call the function and print the output
output = find_fittest_trainees(oxygen_levels)
print(output)
