import csv
import sys

#Getting ID/Username
userInput = input("Enter ID or Username: ")

#Extracting data from users-sorted.csv
data = csv.reader(open('users-sorted.csv', "r"), delimiter=",")
header = next(data)
print(header)

flag = False

#checking for ID/Username
for row in data:
    if userInput == row[0] or userInput == row[3]:
        for title,details in zip(header,row):
            print(title + ": " + details)
        flag = True
        break

if(not flag):
    print("Invalid ID or Username!")

