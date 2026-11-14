word = input("Enter your word: ")

word = word.lower()

if word == word[::-1]:
    print("Entered word is palindrome")
else:
    print("Entered word is not palindrome")
