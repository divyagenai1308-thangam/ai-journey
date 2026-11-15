
#students_grade
students = [
    {"name":"Iniya", "score":96},
    {"name":"Naresh", "score":100},
    {"name":"Rajadurai", "score":78},
    {"name":"Divya", "score":56},
    {"name":"Anandhi", "score":35},
    {"name":"Saranya", "score":-89}
]

def get_grade(score):
    if score < 0 or score > 100:
        return "Invalid Score"
    elif score >= 90:
        return "A"
    elif score >= 70:
        return "B"
    elif score >=40:
        return "C"
    else:
        return "Fail"

total =0
highest_score = 0
count = len(students)
print(count)
for s in students:
   print("Name: ",s["name"], "Score: ",s["score"], "Grade: ",get_grade(s["score"]))
   total = total + s["score"]
   
   if highest_score < s["score"]:
       highest_score = s["score"]
       highest_score_name = s["name"]
print("highest_score is: ",highest_score)
print("Top Scorer is: ", highest_score_name)
Average = total/count
print("Class Average is: ", int(Average))








    


