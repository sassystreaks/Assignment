def shortestPalindrome(s):
    # Find the longest palindrome starting from the beginning of the string
    i = 0
    for j in range(len(s) - 1, -1, -1):
        if s[i] == s[j]:
            i += 1
    
    # If the string is already a palindrome, return the original string
    if i == len(s):
        return s
    
    # Construct the shortest palindrome by adding the reverse of the remaining part
    # to the front of the string
    return s[j+1:][::-1] + s

# Take user input for the string
user_input = input("Enter a string: ")

# Get the shortest palindrome for the user-provided input
result = shortestPalindrome(user_input)
print("Shortest palindrome:", result)
