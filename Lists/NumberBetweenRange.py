
num = []
for i in range(2000,3201):
    if(i%7==0 ) & (i%5 != 0):
        num.append(i)
print(list(num))
