#FUNCTION to calculate average
def get_avg(marks):
    return sum(marks)/len(marks)
#function to calculate total average
def calculate_tot_avg(students):
    assign=get_avg(students ["assignment"])
    test=get_avg(students["test"])
    lab=get_avg(students["lab"])
#Return the result based on weightage given
#10% of assignment,70% of test,20% of lab
    return 0.1*assign+0.7*test+0.2*lab
#calculate grade for each student
def assign_grade(score):
    if score>=90: return"A"
    elif score>=70: return"B"
    elif score>=50: return"C"
    else: return"E"
#Function to calculate total average marks
#for the whole class
def class_avg(studlist):
    rlist=[]
    for s in studlist:
        savg=calculate_tot_avg(s)
        rlist.append(savg)
    return get_avg(rlist)

#create the dictionary of student records
trusha = { "name":"Trusha Salian",
"assignment" : [90, 90, 90, 90],
"test" : [95, 95],
"lab" : [90.10, 90.10]}


chrishanth = { "name":"Chrishant Lukshmanraj",
"assignment" : [82, 76, 48, 50],
"test" : [90, 90],
"lab" : [66.30, 66.42]
}

deepesh = { "name":"Deepesh Durgam",
"assignment" : [82, 76, 48, 50],
"test" : [90, 90],
"lab" : [99, 99]
}

meet = { "name":"Meet Gangwal",
"assignment" : [82, 76, 48, 50],
"test" : [90, 90],
"lab" : [35, 36]
}

karthik = { "name":"Karthik Aaryan",
"assignment" : [82, 76, 48, 50],
"test" : [90, 90],
"lab" : [89, 56.42]
}
#student list consisting of the
#dictionary of all students
students=[trusha,chrishanth,deepesh,meet,karthik]
#iterate through the students list
#and calculate their respective
#average marks and grade
for i in students:
    print(i["name"])
    print("----------------------------")
    print("Average Marks of",i["name"],"is",
             calculate_tot_avg(i))
    print("Grade of ",i["name"],"is:",assign_grade(calculate_tot_avg(i)))
    print()
print("Average Marks of the whole class is",class_avg(students))
