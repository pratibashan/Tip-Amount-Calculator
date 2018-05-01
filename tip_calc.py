#calculating tip amount

total = float(input("Enter the total amount: "))
tippercent=float(input("Enter the tip percentage: "))

# formatting the numbers into 2 decimal points
tipamount =format((total * tippercent),".2f") 

print (f"The tip amount is {tipamount}")