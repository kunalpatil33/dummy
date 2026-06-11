unit = int(input("Enter electricity units :"))

if unit <= 100:
    bill=unit * 5 
elif unit <= 200:
    bill = (100*5)+((unit-100)*7)
else:
    bill = (100*5)+(100*7)+((unit-200)*10)

gst = bill * 0.18
total_bill = bill + gst

print("Electricity bill =",bill)
print("GST(18%)=",gst)
print("Total bill =",total_bill)