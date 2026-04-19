# Function to print Fibonacci series up to n terms
def fibonacci(n):
    # Initialize first two Fibonacci numbers
    a = 0  # First number
    b = 1  # Second number

    # Loop to generate n terms
    for i in range(n):
        print(a)  # Print current Fibonacci number

        # Update values for next iteration
        temp = a + b  # Next number is sum of previous two
        a = b         # Move b to a
        b = temp      # Move new value to b


# Take input from user
n = int(input("Enter number of terms: "))

# Call the function
fibonacci(n)