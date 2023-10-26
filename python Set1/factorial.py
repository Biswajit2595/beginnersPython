def factorial(n):
    if n<0:
        return 'Factorial is not defined for negetive numbers.'
    elif n==0:
        return 'Factorial of 0 is 1.'
    else:
        result=1
        for a in range(1,n+1):
            result*=a
        return f'Factorial of {n} is {result}'
    

number=5;
print(factorial(number))