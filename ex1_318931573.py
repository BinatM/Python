''' Exercise #1 - solution. Python.'''

#########################################
# Question 1 - do not delete this comment
#########################################
S = 220.0
AB = 20.0
BC = 10.0
AD = 15.0
DC = 35.0
# Write the rest of the code for question 1 below here.
Perimeter = AB + BC + AD + DC
MiddleEF = 0.5*(AB+DC)
H = S/MiddleEF

print("Perimeter is: " + str(Perimeter))
print("Midsegment is: " + str(MiddleEF))
print("Height is: " + str(H))


#########################################
# Question 2 - do not delete this comment
#########################################
my_name = "tom"
# Write the rest of the code for question 2 below here.
print("Hello " + my_name.capitalize() + "!")


#########################################
# Question 3 - do not delete this comment
#########################################
number = str(-83)
# Write the rest of the code for question 3 below here.
if int(number) % 7 == 0:
    print("I am " + number + " amd i am divisible by 7")
else:
    print("I am " + number + " amd i am not divisible by 7")


#########################################
# Question 4 - do not delete this comment
#########################################
text = "tom"
copies = 3
# Write the rest of the code for question 4 below here.
i = 0
str1 = text[::2]
str2 = text[1::2]
new_str = str1 + str2
print(new_str*copies)


#########################################
# Question 5 - do not delete this comment
#########################################
name = "droLtromedloV"
q = 4
# Write the rest of the code for question 5 below here.

if q < 0 or q >= len(name) or name == "":
    print("Error: illegal input!")
else:
    sub1 = name[:q]
    sub2 = name[q:]
    temp1 = ""
    i = 1
    while i <= q:
        temp1 = temp1+sub1[q-i]
        i = i+1
    sub1 = temp1
    i = 1
    temp1 = ""
    while i <= len(sub2):
        temp1 = temp1+sub2[len(sub2)-i]
        i = i+1
    sub2 = temp1
    print(sub1 + " " + sub2)
