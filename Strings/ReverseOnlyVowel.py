#Reverse on vowel from given string

sentence = input("Enter the string: ")
vol = []
for letter in sentence:
    if letter in "aeiouAEIOU":
        vol.append(letter)
reversed = vol[::-1]
#Iterator for the reversed vowels
#reversed_vowel = iter(reversed)
i = 0
result = []
for letter in sentence:

    if letter in "aeiouAEIOU":
        #next() function is used to get the next item from the iterator reversed_vowel
        result.append(reversed[i])
        i=i+1
    else:
        result.append(letter)
print(''.join(result))


