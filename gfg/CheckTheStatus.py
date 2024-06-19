# Read input values
a = int(input())
b = int(input())
flag = True
# Check the conditions
if (a >= 0 and b < 0 and not flag) or (a < 0 and b >= 0 and not flag):
    print("True")
elif a < 0 and b < 0 and flag:
    print("True")
else:
    print("end")
