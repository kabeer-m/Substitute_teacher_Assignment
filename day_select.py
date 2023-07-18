from tkinter import *
from functions_file import getday

day = getday()

def day_select():

    def which_day(x):
        global day
        day = x
        
        day_label.configure(text = day)

    def stop():
        root2.destroy()

    root2 = Tk()                            #this is named root2 as 
    root2.geometry("500x200")
    root2.title('PLEASE SELECT DAY')
    
    day_label = Label(root2, text=day)      #the updating text in the menu
    day_label.pack()

    #button for each day

    mon= Button(root2,text = 'MONDAY',command =lambda :  which_day('Mon'),bg = 'black',fg='white')
    mon.pack(fill=(X))
    tue= Button(root2,text = 'TUESDAY',command =lambda :  which_day('Tue'),bg = 'black',fg='white')
    tue.pack(fill=(X))
    wed= Button(root2,text = 'WEDNESDAY',command =lambda :  which_day('Wed'),bg = 'black',fg='white')
    wed.pack(fill=(X))
    thu= Button(root2,text = 'THURSDAY',command =lambda :  which_day('Thur'),bg = 'black',fg='white')
    thu.pack(fill=(X))
    fri= Button(root2,text = 'FRIDAY',command =lambda :  which_day('Fri'),bg = 'black',fg='white')
    fri.pack(fill=(X))
    sat= Button(root2,text = 'SATURDAY',command =lambda :  which_day('Sat'),bg = 'black',fg='white')
    sat.pack(fill=(X))

    done = Button(root2,text = 'DONE',command = stop,bg = 'brown',fg='white').pack(fill=(X))

    root2.mainloop()

    return(day)

