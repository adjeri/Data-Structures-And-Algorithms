# Given two strings,  and , that may or may not be of the same length, determine the minimum number of character deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.

def makeAnagram(a, b):
    dico = {}
    for element in a:
        if element in dico:
            dico[element] += 1
        else:
            dico[element] = 1

    for element in b:
        if element in dico:
            dico[element] -= 1
        else:
            dico[element] = -1

    somme = 0

    for el in dico:
        somme += abs(dico[el])

    return somme

a = 'cde'
b = 'abc'
print(makeAnagram(a,b))