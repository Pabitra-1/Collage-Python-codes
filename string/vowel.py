def is_vowel(ch):
    return ch.lower() in "aeiou"

string = input("Enter the string: ")

vowels = 0
consonants = 0

for ch in string:
    if ch.isalpha():
        if is_vowel(ch):
            vowels += 1
        else:
            consonants += 1

print("Number of vowels in the string is:", vowels)
print("Number of consonants in the string is:", consonants)