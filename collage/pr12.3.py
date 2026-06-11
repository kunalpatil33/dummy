data = {'a': 10, 'b': 50, 'c': 30, 'd': 90, 'e': 70}

# Sort values in descending order and take top 3
highest_three = sorted(data.values(), reverse=True)[:3]

print("The highest 3 values are:", highest_three)