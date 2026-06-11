speed = int(input("Enter speed of vehical :"))

if speed < 40 :
    print("safe")
elif speed <= 80 :
    print("normal")
elif speed <= 120:
    print("Warning !")
else:
    print("challan + License Suspention")
