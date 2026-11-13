#Tip splitter: Ask for a bill amount, a tip percentage and the number of people. Print how much each person pays. (Hint: convert with float() for the bill and tip, and int() for people.)

bill_amount = float(input("What's your bill amount?"))
tip_percentage = float(input("Tip percentage please?"))
ppl_count = int(input("No. of people?"))

final_amt = bill_amount + (bill_amount * tip_percentage/100)
pay_each = final_amt/ppl_count

print(f"Each person billa amount is {pay_each:.2f} ")