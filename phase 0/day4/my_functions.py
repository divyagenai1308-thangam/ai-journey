def is_even(n):
    return n%2 == 0

def is_palindrome(word): 
    word = word.lower()
    return word == word[::-1].lower()

def count_vowels(text):
    text = text.lower()
    count=0
    for ch in text:
        if ch in "aeiou":
            count = count+1
    return count

print(is_even(0))
print(is_even(-4))
print(is_even(7))
print(is_palindrome("MadaM"))
print(is_palindrome("Even"))
print(is_palindrome(""))
print(is_palindrome("ab"))
print(count_vowels("aEIou"))
print(count_vowels("rhythm"))