def reverse(s):
    if not s or not len(s) or type(s) != str:
        return "hmmm that's not a string"

    backward = []
    totalItem = len(s) - 1
    i = totalItem
    while i >= 0:
        backward.append(s[i])
        i-=1

    return ''.join(backward)

print(reverse('Hi my name is Adjeri'))