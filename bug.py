def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage with potential error:
my_list = []
result = calculate_average(my_list)
print(f"The average is: {result}")

my_list = [1,2,3,4,5]
result = calculate_average(my_list)
print(f"The average is: {result}")

my_list = [1,2,'a',4,5]
result = calculate_average(my_list)
print(f"The average is: {result}")