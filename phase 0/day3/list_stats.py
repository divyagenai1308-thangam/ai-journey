num = input("Enter numbers separated by space: ")

final = []
num = num.split()
for item in num:
    final.append(float(item))

Count = len(final)

if Count==0:
    print("No numbers Entered")
else:
    Total = sum(final)
    Maximum = max(final)
    Minimum = min(final)
    Average = Total/Count
    print(f" Count: {Count}, Sum: {Total:.2f}, Maximum; {Maximum:.2f}, Minimum: {Minimum:.2f}, Average: {Average:.2f} ")

