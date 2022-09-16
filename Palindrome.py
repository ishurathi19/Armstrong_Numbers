# WAP to check whether the given number is palindrome or not
n = int(input("Enter a number "))
x, a = n, 0
while x != 0:
    y = x % 10
    a = a*10 + y
    x //= 10
if n == a:
    print("Number is Palindrome")
else:
    print("Number is not palindrome ")