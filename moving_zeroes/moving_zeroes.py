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


# def moving_zeros(arr):
#if left is zero and right is non-zero
# don't swap
# if left is non-zero increment left,
# if right is zero decrement right

#initialize a left and right pointer
# left is 0
# right is last index in array

# use a while loop
# while left <= right
# if left points at a zero and right points at a non-zero
# swap left and right items in original arr
# increment left
# decrement right
# else
# if left is non-zero
# increment left
# if right is zero:
# decrement right

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")