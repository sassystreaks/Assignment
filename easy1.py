# Define the function to calculate the length of the last word
def lengthOfLastWord(s: str) -> int:
    length = 0
    i = len(s) - 1
    while i >= 0 and s[i] == ' ':
        i -= 1
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1
    return length

#  here the user will be providing a string as an input, the output returned will be equal to the length of the last word in the string
user_input = input("Enter a string: ")
result = lengthOfLastWord(user_input)
print("Length of last word:", result)
