#Tip & Bill splitter

#Making different variables to store values.
_bill=float(input("Enter the bill: "))
_tip=float(input("Enter the tip (Percentage eg., 10, 15, 20): "))
_persons=int(input("Total persons are: "))

#Calculations using different operators
tip_amount=_bill * (_tip/100)
total_amount=_bill + tip_amount
per_person_share=total_amount / _persons

#To display value on the output screen by using print() function.
print(f"Tip amount: {tip_amount :.2f}")
print(f"Total amount - Including tip: {total_amount :.2f}")
print(f"Each person has to pay: {per_person_share:.2f}")
