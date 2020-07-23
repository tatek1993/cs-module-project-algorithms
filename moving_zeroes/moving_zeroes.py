'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here
    # We sort the list, then iterate through it
    # for num in arr if num == 0, add to zeros, else add to numbers array
    # append zeros array to numbers array
    arr.sort()
    zeros = []
    numbers = []

    for num in arr:
        if num == 0:
            zeros.append(num)
        elif num != 0:
            numbers.append(num)

    numbers = numbers + zeros
    return numbers

    pass


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")