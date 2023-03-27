def twoSum(nums, target):
    """ Return an array with the indices of two
    numbers in the list `nums` that add up to 
    the `target`. If there are no two numbers
    that meet the condition, it returns `None`.
    
    Args:
    -----
        
        - nums [ list ] : list of integers in which 
        to search for the two numbers.
        
        - target [ int ] : integer that represents 
        the sum goal.
    
    Returns:
    --------
    
        - result [ array | None ] : a list with two integers 
        representing the indices of the two numbers
        that add up to `target`, or `None` if they
        are not found.
        
    Example:
    --------
    
        >>> nums = [2, 7, 11, 15]
        >>> target = 9
        >>> twoSum(nums, target)
        [0, 1]

        >>> nums = [3, 2, 4]
        >>> target = 6
        >>> twoSum(nums, target)
        [1, 2]

        >>> nums = [3, 3]
        >>> target = 6
        >>> twoSum(nums, target)
        [0, 1]
        
    """
    hashmap = {}
    #print(f"input nums:{nums}, and target: {target}")
    for i, num in enumerate(nums):
        complement = target - num
        #print(f"{i} --> target: {target} - num: {num} = {complement}")
        if complement in hashmap:
            #print(f"{i} --> if {complement} in {hashmap}")
            return [hashmap[complement], i]
        hashmap[num] = i
        #print(hashmap)
        #print(hashmap[num])
        #print(hashmap[num], i)
        #print(f"complement: {complement}")
    return None

nums = [3, 11, 2, 9, 15, 2, 7]
#print(type(nums))
target = 9
result = twoSum(nums, target)
print(result)
#print(type(result))

""" 
Explanation:
------------
    
    input = [3, 11, 2, 9, 15, 2, 7]
    
    Given an array of integers nums and an 
    integer target, return indices of the 
    two numbers such that they add up to 
    target.

    You may assume that each input would 
    have exactly one solution, and you may 
    not use the same element twice.

    You can return the answer in any order.
    
    i : 0 
    hashmap = {3: 0}
    result: hashmap = {3: 0} - {target[9]} = 6
    complement = 6 *if next iter the content is [6] end the loop and return result.
    
    i : 1
    hashmap = {3: 0, 11: 1}
    result: hashmap = {11: 1} - {target[9]} = -2
    complement = -2 *if next iter the content is [-2] end the loop and return result.
    
    i : 2
    hashmap = {3: 0, 11: 1, 2: 2}
    result: hashmap = {2: 2} - {target[9]} = 7
    complement = 7 *if next iter the content is [7] end the loop and return result.
    
    i : 3
    hashmap = {3: 0, 11: 1, 2: 2, 9: 3}
    result: hashmap = {9: 3} - {target[9]} =  0
    complement = 0 *if next iter the content is [0] end the loop and return result.
    
    i : 4
    hashmap =  {3: 0, 11: 1, 2: 2, 9: 3, 15: 4}
    result: hashmap = {15: 4} - {target[9]} = -6
    complement = -6 *if next iter the content is [-6] end the loop and return result.
    
    i : 5
    hashmap = {3: 0, 11: 1, 2: 5, 9: 3, 15: 4, 2: 5}
    result: hashmap = {2: 5} - {target[9]} = 7
    complement = 7 *if next iter the content is [7] end the loop and return result.
    
    i : 6
    hashmap = {3: 0, 11: 1, 2: 5, 9: 3, 15: 4, 2: 5, 7: 6}
    complement = the next iter is [7] end the loop and return result.
    END / break

Return = [5, 6]

"""