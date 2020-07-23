'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n, cache):
    # Your code here
    # base cases
    if n < 0:
        return 0
    elif n == 0:
        return 1
        # check if the work has already been done
        # by looking at the cache
    elif cache is not None and cache[n] > 0:
        # return the previously computed answer and dont recurse
        return cache[n]
    else:
        if cache is None:
            
        eat_1 = eating_cookies(n - 1)
        eat_2 = eating_cookies(n - 2)
        eat_3 = eating_cookies(n - 3)
        return eat_1 + eat_2 + eat_3

    pass


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies"
    )
