'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # Your code here
    # sort the array
    arr.sort()
    # the index
    i = 0

    # loop through the array after we've sorted it
    while i < len(arr):
        # if the index is equal to the next index, then skip the next index because they are duplicates
        if arr[i] == arr[i + 1]:
            i += 2
        elif arr[i] != arr[i + 1]:
            return arr[i]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")