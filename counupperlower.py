def countupperlower(string):
    upper_case = 0
    lower_case = 0
    for i in string:
        if i.isupper():
            upper_case = upper_case + 1
        elif i.islower():
            lower_case = lower_case + 1
        else:
            pass
    print('upper case is', upper_case)
    print('lower case is', lower_case)

countupperlower('The quick Brow Fox')