

# Vowel count

sentence = input("Enter your sentence here: ").lower()
count = 0

for ch in sentence:
    if ch in "aeiou":
        count = count+1
print(count)
