#Grde_checker

score = int(input("Enter your score: "))

if score < 0 or score >100:
    print("Invalid Score")
elif score >= 90 and score <= 100:
    print("Your Grade is A")
elif score >= 75:
    print("Your Grade is B")
elif score >= 50:
    print("Your Grade is C")
else:
    print("You are Fail")

