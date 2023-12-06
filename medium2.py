from collections import Counter

def majorityElement(nums):
    n = len(nums)
    count = Counter(nums)
    result = []
    
    # Find elements that appear more than floor(n/3) times
    for key, val in count.items():
        if val > n // 3:
            result.append(key)
    
    return result

# Take user input for the array of integers
user_input = input("Enter the integers separated by spaces: ")
nums = list(map(int, user_input.split()))

# Get the elements appearing more than floor(n/3) times
result = majorityElement(nums)
print("Elements appearing more than ⌊n/3⌋ times:", result)
