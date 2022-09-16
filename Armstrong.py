# WAP to check whether the number is armstrong
n = int(input("Enter a number "))
a, s = 0, 0
i, z = n, n
while i != 0:
    a += 1  # use to count digits in a number
    i = i // 10
while z != 0:
    y = z % 10
    s += (y ** a)
    z = z // 10
if n == s:
    print("Number is armstrong")
else:
    print("Number is not armstrong")
