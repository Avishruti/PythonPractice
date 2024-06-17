#With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.

num = int(input("Enter the number: "))
n = {}
for i in range(1,num+1):
    n[i] = i * i
print(n)
