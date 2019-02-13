
# https://raw.githubusercontent.com/prof-rossetti/georgetown-opim-243-201901/master/data/gradebook.json

# goal: calculate average grade

import json
import requests
import statistics

request_url = "https://raw.githubusercontent.com/prof-rossetti/georgetown-opim-243-201901/master/data/gradebook.json"

response = requests.get(request_url) #storing the response in a variable

parsed_response = json.loads(response.text) #using the JSON package to parse it (dictionary)

# breakpoint() #use this interactive feature to investigate the code above

grades = []

#l = [90, 80, 70]
#print(statistics.mean)

for student in parsed_response["students"]: #student will be a dictionary and students will be a list
   # print(type(student), student)
    grades.append(student["finalGrade"]) # to add another attribute to our list
    #print(grades) # now we have the grades, but we want the mean.

avg_grade = statistics.mean(grades)
print("THE AVERAGE GRADE IS: " + str(avg_grade))

