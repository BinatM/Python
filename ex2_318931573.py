""" Exercise #2. Python for Engineers."""

#########################################
# Question 1 - do not delete this comment
#########################################

a = 2
lst = [1 ,2 ,3 ,4 ,5] 

# Write the rest of the code for question 1 below here.
n=0
i=0
while n<2 and i<len(lst):
    if lst[i]%a==0:
        n=n+1
    i=i+1
if n==2:
    print (i-1)
else:
    print ("-1")
            

# End of code for question 1

#########################################
# Question 2 - do not delete this comment
#########################################
lst2 = ['hello', 'world', 'course', 'python', 'day']

# Write the code for question 2 using a for loop below here.
sum=0
avg = 0
for s in lst2:
    sum = sum + len(s)
avg = sum/len(lst2)
sum = 0
for s in lst2:
    if len(s)>avg:
        sum = sum+1
print("The number of strings longer than the average is:", str(sum))

# Write the code for question 2 using a while loop below here.

i=0
sum=0
avg=0
while i<len(lst2):
    sum = sum + len(lst2[i])
    i = i+1
avg = sum/len(lst2)
sum = 0
i=0
while i<len(lst2):
    if len(lst2[i])>avg:
        sum = sum+1
    i=i+1
print("The number of strings longer than the average is:", str(sum))

# End of code for question 2

#########################################
# Question 3 - do not delete this comment
#########################################

lst3 = [1 ,2 ,3 ,4 ,5]  # Replace the assignment with other lists to test your code.


# Write the rest of the code for question 3 below here.
i=0
total=0
if len(lst3)==0:
    print("0")
elif len(lst3)==1:
    print(lst3[0])
else:
    while i<len(lst3)-1:
        total =total + lst3[i]*lst3[i+1]
        i=i+1
    print(total)


# End of code for question 3


#########################################
# Question 4 - do not delete this comment
#########################################

lst4 = [1, 3, 0, 2]    # Replace the assignment with other lists to test your code.

# Write the rest of the code for question 4 below here.
i=1
maxh=0
new_lst = [lst4[i-1]]
while i<len(lst4):
    if abs(lst4[i]-lst4[i-1])>maxh:
        maxh = abs(lst4[i]-lst4[i-1])
        new_lst.append(lst4[i])
    i=i+1
print(new_lst)


# End of code for question 4

#########################################
# Question 5 - do not delete this comment
#########################################

my_string = 'abaadddefggg'  # Replace the assignment with other strings to test your code.
k = 4  # Replace the assignment with a positive integer to test your code.

# Write the rest of the code for question 5 below here.
i=0
new=""
temp=""
while i<len(my_string)-1:
    temp = my_string[i]*k
    if temp in my_string:
        print(f"For length {k}, found the substring {temp}!")
        break
    i=i+1
if i==len(my_string)-1:
    print("Didn't find a substring of length", str(k))


# End of code for question 5
