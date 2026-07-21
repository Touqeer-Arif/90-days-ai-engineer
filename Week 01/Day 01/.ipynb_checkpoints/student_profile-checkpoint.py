#Student Profile Generator

full_name = str(input("Enter your Full Name:"))
father_name = str(input("Enter your Father's Name:"))
uni_name = str(input("Enter your University Name:"))
degree_name = str(input("Enter your Degree Name:"))
semester_no = int(input("Enter your Semester Number:"))
age = int(input("Enter your Age:"))
cgpa = float(input("Enter your current CGPA:"))
city = str(input("Enter your Current City of Residence:"))
country = str(input("Enter your Current Country of Residence:"))

if cgpa >= 3.5:
    performance = "Outstanding Performance"
elif cgpa >= 3.0:
    performance = "Good Performance"
else:
    performance = "Needs Improvement"

semester_left = 8 - semester_no
if semester_left == 0:
    year_left = "Your Degree is Completed"
elif semester_left == 1:
    year_left = "Half of an Year"
elif semester_left == 2:
    year_left = "An Year"
elif semester_left == 3:
    year_left = "One and a Half Year"
elif semester_left == 4:
    year_left = "Two Year"
elif semester_left == 5:
    year_left = "Two and a Half Year"
elif semester_left == 6:
    year_left = "Three Year"
elif semester_left == 7:
    year_left = "Three and a Half Year"
print()
print("         STUDENT PROFILE")
print()
print(f"Student Name : {full_name}")
print(f"Father Name  : {father_name}")
print(f"University   : {uni_name}")
print(f"Degree       : {degree_name}")
print(f"Semester     : {semester_no}")
print(f"Age          : {age}")
print(f"CGPA         : {cgpa}")
print(f"City         : {city}")
print(f"Country      : {country}")
print(f"Performance  : {performance}")
print(f"Years Left   : {year_left}")