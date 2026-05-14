# Define the function
def number_pattern(n):
  
	# Check if the argument in NOT an integer
	if not isinstance(n, int):
		return "Argument must be an integer value."
	
	# Check if the integer is less than 1
	if n < 1:
		return "Argument must be an integer greater than 0."
