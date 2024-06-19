#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line

num = int(input("Enter number: "))
fac = 1
fact = []
for i in range (1,num+1):
    fac = fac * i
    fact.append(fac)
print(','.join(map(str,fact)))

