set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

print("Set 1:", set1)
print("Set 2:", set2)

# Intersection
print("\nIntersection of sets:", set1.intersection(set2))

# Union
print("Union of sets:", set1.union(set2))

# Set Difference (elements in set1 but not in set2)
print("Difference of sets (set1 - set2):", set1.difference(set2))

# Symmetric Difference (elements not common in both)
print("Symmetric Difference:", set1.symmetric_difference(set2))

# Clearing a set
set1.clear()
print("\nSet 1 after clearing:", set1)