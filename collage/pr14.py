def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

# Function using **kwargs
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

# Main Program
print("Sum of numbers:", add_numbers(10, 20, 30, 40))

print("\nStudent Details:")
print_details(name="Kunal", age=17, course="Computer Science")