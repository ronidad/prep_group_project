from functions import *
students = {'John':50, 'James':60}



temprature = [10,20,30,40,50]

print("the mean for " +str(len(students)) + " students is " + str(mean(students)  ) )

print("The average temprarure is " +  str(mean(temprature)))

for student in students.keys():
    #you can also use students.items to get key value pair
    print(student)

phone_numbers = {"Ronald": " 725029795", "Benard": " 724648426"}
for value in phone_numbers.values():
    print(value.replace(" ", "254"))

# password = ""
# while password !="password":
#     password=input("Enter password")
# while True:
#     username= input("Enter username ")
#     if username == "ron":
#         break
#     else:
#         continue


    