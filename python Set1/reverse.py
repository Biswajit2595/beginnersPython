def reverse(str):
    rev_str=""
    for a in str:
        rev_str=a+rev_str
    return rev_str

input="Python"
rev=reverse(input)

print(rev)