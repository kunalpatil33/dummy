x = {}
stud ={
    "name":"kunal",
    "age":18,
    "div":"D",
    "marks":[97,98,99],
    "rollno":37,
}

print(stud.keys())
print(stud.values())
print(stud.items())

for values in stud.values():
    if type(values)==list:
        for i in values:
         print(i)
         continue
        print(values)


