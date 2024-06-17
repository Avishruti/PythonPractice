#Reverse vowel and print along with constant

sentence = input("Enter the string: ")
vol = []
con = []
for letter in sentence:
    if letter in "aeiouAEIOU":
        vol.append(letter)
    else:
        con.append(letter)
reversed1 = vol[::-1]
print ("".join(reversed1) + "".join(con))




