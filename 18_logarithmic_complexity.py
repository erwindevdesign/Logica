# O(n log n)
nums = [1,2,3,4,5,6,7,8,9]
target = [3]

def binary_search(list):
    left_indicator = 0
    right_indicator = len(nums) - 1

    while left_indicator <= right_indicator:
        half = (left_indicator + right_indicator) // 2
        if nums(half) == target:
            return half
        
        elif nums[half] < target:
            left_indicator = half +1

        else: right_indicator = half - 1
    return -1

print(binary_search)
print(type(binary_search))
print[list[binary_search]]
