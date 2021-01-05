def printParenthesis(n):
    str = [""] * 2 * n;
    return displayParenthesis(str, 0, n, 0, 0)

def displayParenthesis(str, pos, n, open, close,array=[]):

    if (close == n):
        line = ''
        for i in str:
            line += i
            print(i, end = "")
        array.append(line)
        print();
        return
    else:
        if(open < n):
            str[pos] = '(';
            displayParenthesis(str, pos + 1, n, open + 1, close, array);
        if(open > close):
            str[pos] = ')';
            displayParenthesis(str, pos + 1, n, open, close + 1, array)
    return array

n = 2;
str = [""] * 2 * n;
print(printParenthesis(n))