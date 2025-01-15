def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0  # Handle empty or non-numeric list
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

# Example usage:
my_list = []
result = calculate_average(my_list)
print(f"The average is: {result}")

my_list = [1,2,3,4,5]
result = calculate_average(my_list)
print(f"The average is: {result}")

my_list = [1,2,'a',4,5]
result = calculate_average(my_list)
print(f"The average is: {result}")
