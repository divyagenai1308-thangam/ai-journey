#41.

def is_even(n):
    if n%2==0:
        return "True"
    else:
        return "False"

#42.

def reverse_string(word):
    new_word = ""
    for ch in word:
        new_word = ch + new_word
    return new_word

result = reverse_string("temp")
print(repr(result))

#43.

def count_character(word, char):
    count = 0
    if len(char)!=1:
        return "Invalid Character"
    else:
       for ch in word.lower():
          if char.lower() == ch:
            count = count + 1
    return count

result = count_character("Banana", "a")
print(result) 

#44.

def maximum(num):
   if len(num) != 0:
    max_num = num[0]
    for n in num:
        if max_num < n:
          max_num = n
    return max_num

result = maximum([4, 4, 4])
print(result)

#46.
def digit_sum(num):
    dig_sum = 0
    while num > 0:
       add = num%10
       dig_sum = dig_sum + add
       num = num//10
    return dig_sum

result = digit_sum(-1234)
print(result)