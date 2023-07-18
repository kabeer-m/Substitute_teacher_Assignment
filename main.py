from select_screen import *
from functions_file import *
from day_select import *

Today = day_select()

Excepted_teachers = []
Excepted_teachers = List_Generator(Excepted_teachers,"Excepted_teachers","black","white")       #The list generator function is called whenever input is to be taken

First_half_absentees = []
First_half_absentees = List_Generator(First_half_absentees,"First_half_absentees","black","yellow")

Second_half_absentees = []
Second_half_absentees = List_Generator(Second_half_absentees,"Second_half_absentees","black","cyan",First_half_absentees)

##Absent = []         # if teacher is in both first half and seco0nd half absentees
##for teacher in Second_half_absentees :
##    if teacher in First_half_absentees :
##        Absent.append(teacher)
##        First_half_absentees.remove(teacher)
##        Second_half_absentees.remove(teacher)
   
Absent_teachers = []
Absent_teachers += (First_half_absentees+Second_half_absentees)          #for already selected complel;ety absent teachers
Absent_teachers = List_Generator(Absent_teachers,"Absent_teachers","black","lime green",Absent_teachers)


Absentees_schedule = Absentees(Absent_teachers,Today,First_half_absentees,Second_half_absentees) #schedule for absentees

Total = []          # list for each substitution

for teacher in Absent_teachers :               #for every absent teacher
    List = assignment(Absent_teachers,teacher,Today,Total,Excepted_teachers,First_half_absentees,Second_half_absentees)  #function from main
    Total.append(List)


make_file(Total,Absentees_schedule,day)


