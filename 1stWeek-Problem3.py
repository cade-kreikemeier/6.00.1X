# Assume s is a string of lower case characters. Write a program that prints the longest substring of s in which the
# letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print Longest
# substring in alphabetical order is: beggh In the case of ties, print the first substring. For example,
# if s = 'abcbcd', then your program should print Longest substring in alphabetical order is: abc

s = 'abcabcdabcde'
currentString = s[0]
longestSubstring = s[0]

for i in range(len(s)-1):
    if s[i] <= s[i+1]:
        currentString += s[i+1]
        if i == len(s) - 2 and len(currentString) > len(longestSubstring):
            longestSubstring = currentString
    else:
        if len(currentString) > len(longestSubstring):
            longestSubstring = currentString
        currentString = s[i+1]

print("Longest substring in alphabetical order is: " + longestSubstring)