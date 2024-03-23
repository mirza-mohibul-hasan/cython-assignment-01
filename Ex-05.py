# Way-01: This dosen't create a copy. It's sort original one from memory location.
numbers = [3, 5, 1, 9, 7, 2, 8]
numbers.sort()
print(numbers)

# Way-02: Here numbers will be sorted in a copy but in memory location it remain unchanged
numbers = [3, 5, 1, 9, 7, 2, 8]
sortedNumbers = sorted(numbers)
print(sortedNumbers)
