amount = int(input("Enter shopping amount :"))
vip = str(input("Are you VIP customer(yes/no) :"))
discount = 0

if amount > 5000 :
    discount =  amount * 20 / 100
 
elif amount > 2000 :    
    discount = amount * 10 / 100

if vip == "yes" :
    discount = discount + (amount * 5 / 100) 

final_amount = amount - discount

gst = final_amount * 18 / 100

bill = final_amount + gst 

print("discount : ",discount)
print("GST : ",gst)
print("Final Bill",bill)    