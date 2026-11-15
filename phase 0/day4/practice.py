def friends(name):
    print(f"My Friend name is {name}")

friends("Saranya")
friends("Rajadurai")


def sum(num1, num2):
    print(f"Sum of {num1} and {num2} is {num1+num2}")

sum(10, 20)    
sum(20, 40)


def sum(num1, num2):
    return num1 + num2

result = sum(10, 20)    
print(result)
print(result*3)


def fruit(name):
    print(f"My fruit name is {name}")

fruit("apple")

def add(a, b):
    return a+b

def multiply(c, d):
    return c*d

def subtract(a, b):
    return a-b

print(add(3,4))

result = multiply(4,5)

print(result)

print(subtract(1,2)*2)

def add(a, b):
    print(a+b)

x = add(3, 4)
print(x)

def add(a, b=3):
    return a+b

print(add(4))
print(add(4,4))

def area_of_rectangle(l,b):
    return l * b

x = area_of_rectangle(2,3)
y = area_of_rectangle(4,5)
print(x, y)

def odd(a):
    return a%2 !=0

print(odd(4))

def cube(n=3):
    result = n * n * n
    return result

print(cube(2))

#Dictionaries

Employees = {
    "name" : "Naresh",
    "code" : 111,
    "Skill": "Java"
}

print(Employees)
Employees["code"] = 1
print(Employees)
Employees["email"] = "abc@gmail.com"
del Employees["code"]
print(Employees["Skill"])
print(Employees)
print(len(Employees))
Employees["code"] = 11
print(Employees)

Employees = {
    "name" : "Naresh",
    "code" : 111,
    "Skill": "Java"
}

print(Employees.get("age", "Not Found"))
print("Java" in Employees)

marks = {"Iniya":100, "Naresh":95, "Divya":78}

for name in marks:
    print(name)

for name,score in marks.items():
    print(f"{name} scored {score}")    

print(marks.keys())
print(marks.values())
print(sum(marks.values()))
print(max(marks.values()))
print(min(marks.values()))
average = sum(marks.values())/  len(marks.values())
print(int(average))

sentence = "Am a good girl nd a happy girl"
counts = {}

for word in sentence.split():
   if word in counts:
    counts[word] = counts[word] + 1
   else:
     counts[word]=1 
print(counts)

sentence = "Am a good girl nd a happy girl"
counts = {}

for word in sentence.split():
  counts[word] = counts.get(word, 0)+1 #get(word, default vlue) if word exists it will throw the existing vlue if word not exists throws the default value
print(counts)

Employees = [
   {"name":"Iniya", "age":12, "code":1},
   {"name":"Naresh", "age":13, "code":2}
]

for e in Employees:
    print(e["name"], e["code"])
