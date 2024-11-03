"""
This Code finds peaks in the array - numbers bigger than their neighbours.
"""

def Find_peaks(array):
    indices = [] # Initiating an empty array to use as answer.

    # The 2 ifs below are for edge cases, in case the first or last numbers are peaks.
    if array[0] > array[1] and array[0] > array[-1]:
        indices.append(0)

    if array[-1] > array[-2] and array[-1] > array[0]:
        indices.append(len(array) - 1)

    for i in range(1, len(array) - 1): #the range does not include the first and last elements.

        if array[i-1] < array[i] > array[i+1]:
            indices.append(i)

    return indices

#I've used this tedious method to enter the array
#yet it ensures that all values are valid.
numbers = []

while True:
    n = input("Please enter a number to add to list, or press 'N' to continue: ")

    if n.upper() == "N": # Exit option for loop.
        break

    elif n.isdigit():
        numbers.append(int(n))

    else:
        print("Please enter a valid value.")

print(f"Original array: {numbers}")
print(Find_peaks(numbers))