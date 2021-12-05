def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    # YOUR CODE HERE
    #  
    num_of_sevens = 0
    for i in nums:
        if i == 7:
            num_of_sevens += 1
    return(num_of_sevens > 0)

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

