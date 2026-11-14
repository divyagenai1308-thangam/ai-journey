word = "chennai"

print(word[::-1])
print(word[:4])

text = " Cutie Pie "

print(text.strip())
print(text.upper())
print(text.lower().strip())
print(text.replace("Cutie", "Chutti"))
print("Laddu" in text)

count = "Laddu"

count = count.upper()

print(count)


sentence = "My Momma is my only world"
word = sentence.split()

print(word)
print(len(word))
print(" ".join(word))

for ch in "Iniyshree":
  print(ch)

word = " Divya "
print(word.strip().upper())
print(len(word))

# List

friends = ["Rajadurai", "Saranya", "Sasi", "abc"]

friends.append("Anandhi")
print(friends)
friends.remove("abc")
friends.insert(1, "Kavi")
print(friends)
print(friends[::-1])
print(len(friends))
print(friends[10])

nums = [90, 87, 101, 99, 12, 1]

print(sum(nums))
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums)/len(nums))


marks = [10, 20, 30]
total = 0

for m in marks:
    total = total+m
print(total/len(marks))

square = []

for i in range(1,6):
    square.append(i*i)
print(square)


nums = input("Enter you numbers separated by space: ")

final = []

for item in nums.split():
    final.append(float(item))

print(final)

n= int(input("Enter how many even numbers you want? "))
num = []

for i in range(2, 2*n+1, 2):
    num.append(i)
print(num)


