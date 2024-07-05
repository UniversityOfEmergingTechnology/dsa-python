# students = ["Harry" , "Ron" , "Hermione" , "Draco" , "Neville"]


# print(students[0])
# print(students[1])
# print(students[2])
# print(students[3])
# print(students[4])

# range function
# len function
# for student in students : 
#     print(student)

# for i in range(len(students)) :
#     print( i + 1 , students[i])


# dictionary 

# students = {
#     "Hermoine" : "Gryffindor",
#     "Ron" : "Griffindor",
#     "Harry" : "Griffindor",
#     "Draco" : "Slytherin",
#     "Luna" : "Ravenclaw"
# }

# print(students["Hermoine"])


# for student in students :
#     print(student , students[student] , sep=" : " )

students = [
    {"name" : "Hermoine" , "house" : "Gryffindor" , "patronus" : "Otter"},
    {"name" : "Ron" , "house" : "Griffindor" , "patronus" : "Jack Russell Terrier"},
    {"name" : "Harry" , "house" : "Griffindor" , "patronus" : "Stag"},
    {"name" : "Draco" , "house" : "Slytherin" , "patronus" : "None"},
    {"name" : "Luna" , "house" : "Ravenclaw" , "patronus" : "Hare"}
]

print(students[2]["patronus"])

for student in students :
    print(student["name"] , student["house"] , student["patronus"] , sep=" : ")
