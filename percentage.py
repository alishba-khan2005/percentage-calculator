print("-----------calculating marks-----------")
#extra information
name=str(input("enter your name: "))
clas=int(input("enter your class: "))
section=str(input("enter our section: "))
#calculating percentage
physics=int(input("enter your physics marks: "))
chem=int(input("enter your chem marks: "))
calculus=int(input("enter your calcalus marks: "))
obtained_marks=physics+chem+calculus
total_marks=100
percentage=obtained_marks*100/total_marks
print(percentage)

if percentage < 50:
    print(percentage,"you have failed")
elif 60>= percentage >=50:
    print(percentage,"you have passed\n your grade is good")
elif 60<= percentage<=80:
    print(percentage,"youhave passed\n your grade is very good")
else:
    print("you have passed the exam\n your grades are outstanding")