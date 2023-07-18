import csv
from tkinter import *


column=5  #these will be used in the display names function,, which is called later
row=0

def List_Generator(List_name,Title,bg_color,fg_color,skip=[]):

    root = Tk()
    root.title(Title)

    px = 10
    py = 10


    #function to display the names of absent teachers
    def display_names(t,c,r):        
        myLabel=Label(root,text=t).grid(row=r,column=c,sticky='w')

    def assign(t):              #function to select 'Excepted' teachers
        global column,row
        if t not in List_name :
            List_name.append(t)
            display_names(t,column,row)
            row+=1
            if row>limit:
                row=0
                column+=1

    def close(r):               #function to close the tkinter root loop
        r.destroy()


    f = open('Teachers-timetable.csv')
    L = []
    start = True
    for i in csv.reader(f):
        if start == True:       #so as to not includethe first row
            start = False
            continue
        if (i[0] not in L):
            L.append(i[0])


    br = 0          #button row number
    bc = 0          #button column number

        
    for teacher in L:
        if teacher in skip:
            continue
        button= Button(root, text = teacher,padx=px,pady=py,
                command=lambda t = teacher: assign(t)
                ,bg = bg_color , fg = fg_color)             #if we use lambda directly
        button.grid(row=br,column=bc,sticky="nsew")         #without assigning the value of the teacher to another variable, 
        bc+=1                                               #it will always store the last teacher in the loop
        if bc > 4:                                          #so we use lambda (k = teacher) : func(k) instead of
            br+=1                                           # lambda:func(teacher)
            bc = 0
    else:
        button= Button(root, text = "DONE",padx=px,pady=py,command=lambda : close(root) ,bg = "brown" , fg = 'white')
        button.grid(row=br,column=bc,sticky="nsew")
        limit = br
        br = 0
        bc = 0                          #resetting the row/columns

    for i in List_name:                 # for displaying names of already selected teachers
        global column,row
        display_names(i,column,row)
        row+=1
        if row>limit:
                row=0
                column+=1


    root.mainloop()

    column = 5
    row = 0
    limit = 0

    return(List_name)
