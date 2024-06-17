#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.

num = []
for i in range(2000,3201):
    if(i%7==0 ) & (i%5 != 0):
        num.append(i)
print(list(num))
