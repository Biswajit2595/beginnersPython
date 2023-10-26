def arrange_lowercase_first(string):
    lower=""
    upper=""
    for a in string:
        if a==a.lower():
            lower+=a
        if a==a.upper():
            upper+=a

    arranged_string = ''.join(lower + upper)

    return arranged_string

# Given input
str1 = "PyNaTive"
result = arrange_lowercase_first(str1)
print(result)
