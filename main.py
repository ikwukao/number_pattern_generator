# Define the function
def number_pattern(n):
    
    pattern = ""

    # Loop from 1 up to n (inclusive)
    for number in range(1, n + 1):
        # Add each number and a space to the string
        pattern += str(number) + " "
        
    # Remove the extra space at the end of the string
    return pattern.strip()

	# Check if the argument in NOT an integer
    if not isinstance(n, int):
        return "Argument must be an integer value."
	
	# Check if the integer is less than 1
    if n < 1:
        return "Argument must be an integer greater than 0."

    # Remove the extra space at the end of the string
    return pattern.strip()


# Test the function with a valid input
print(number_pattern(4))
