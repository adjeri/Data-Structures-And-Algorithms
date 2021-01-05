# You are given a string containing characters A and B only. Your task is to change it into a string such that there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.Your task is to find the minimum number of required deletions.

def alternatingCharacters(s):
    number = 0
    old=s[0]
    for i in range(1,len(s)):
        if s[i] != old:
            old = s[i]
        else:
            number += 1
    return number

print(alternatingCharacters('ABABABAB'))